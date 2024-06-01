# starlark is used instead of more readable YAML because protocols will be added/removed in future.
# you need to set the drone config path to `utils/drone.star` in the webui and also store the ssh key as a drone secret in `ssh_private_key` variable.
# run custom build with force_rebuild parameter set to true to rebuild and override images on registry

def main(ctx):

	protocols = [
		'xray',
		'hysteria',
		'ocserv',
		'sshvpn'
	]

	pipelines = [
		pipeline_1(),
		pipeline_2(protocols)
	]

	return pipelines

def pipeline_1():
	steps = []

	# step 1: check if image exists on remote registry
	steps.append({
		"name": "check_image",
		"image": "alpine:latest",
		"commands": [
			' wget http://registry.opviel.de/v2/_catalog -O - | grep -q "alpine_ansible_hugo" && [ "$force_rebuild" != "true" ] && echo -n "\nBUILD SKIPPED" && exit 78 || exit 0'
		],
		"branch": "master"
	})

	# step 2: if doesn't exist, build and publish image to registry
	steps.append({
		"name": "publish_on_registry",
		"image": "plugins/docker",
		"settings": {
			"repo": "registry.opviel.de/alpine_ansible_hugo",
			"dockerfile": "utils/Dockerfile",
			"registry": "registry.opviel.de",
			"tags": ["latest"],
			"insecure": "true",
			"purge": "true",
			"compress": "true"
		}
	})

	return {
		"kind": "pipeline",
		"type": "docker",
		"name": "Build and Publish Image",
		"platform": { "arch": "arm64" },
		"steps": steps,
		"branch": "master"
	}


def pipeline_2(protocols):

	environment_vars = {
		"SSH_PRIVATE_KEY": {
			"from_secret": "ssh_private_key"
		}
	}

	steps = []

	# step 1: export ssh private key to file
	steps.append({
		"name": "export_ssh_key",
		"image": "alpine",
		"commands": [
			'echo "$SSH_PRIVATE_KEY" > .ssh_private_key',
			"chmod 600 .ssh_private_key"
		 ],
		"environment": environment_vars
	})

	# step 2: add theme
	steps.append({
		"name": "git_add_theme",
		"image": "alpine/git",
		"commands": [
			"git submodule add https://github.com/alex-shpak/hugo-book web/themes/hugo-book",
			"git submodule update --recursive"
		 ],
		"environment": environment_vars
	})

	# step 3: run pipeline
	web_deps = ["export_ssh_key", "build_hugo", "git_add_theme"]
	for protocol in protocols:
		steps.append({
			"name": "setup_{}".format(protocol),
			"image": "registry.opviel.de:80/alpine_ansible_hugo:latest",
			"commands": [
				"/usr/bin/ansible-playbook reactance.yaml -t {}".format(protocol)
			],
			"depends_on": ["export_ssh_key", "build_hugo"]
		})

		web_deps.append("setup_{}".format(protocol))
	steps.append({
		"name": "setup_dns",
		"image": "registry.opviel.de:80/alpine_ansible_hugo:latest",
		"commands": [
			"/usr/bin/ansible-playbook reactance.yaml -t dns"
		],
		"depends_on": ["export_ssh_key", "build_hugo"]
	})

	steps.append({
		"name": "setup_web",
		"image": "registry.opviel.de:80/alpine_ansible_hugo:latest",
		"commands": [
			"/usr/bin/ansible-playbook reactance.yaml -t web"
		],
		"depends_on": web_deps
	})

	return {
		"kind": "pipeline",
		"type": "docker",
		"name": "Execute Playbook",
		"platform": { "arch": "arm64" },
		"steps": steps,
		"depends_on": ["Build and Publish Image"],
		"branch": "master"
	}
