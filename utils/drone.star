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
			"wget http://registry.opviel.de/v2/_catalog -O - | grep -q 'alpine_ansible' && echo -n '\nBUILD SKIPPED' && exit 78 || exit 0"
		],
		"branch": "master"
	})

	# step 2: if doesn't exist, build and publish image to registry
	steps.append({
		"name": "publish_on_registry",
		"image": "plugins/docker",
		"settings": {
			"repo": "registry.opviel.de/alpine_ansible",
			"dockerfile": "utils/Dockerfile",
			"registry": "registry.opviel.de",
			"tags": ["latest"],
			"insecure": "true",
			"purge": "true",
			"compress": "true",
			"mtu": "1400"
		}
	})

	return {
		"kind": "pipeline",
		"type": "docker",
		"name": "Build and Publish Image",
		"platform": { "arch": "arm64" },
		"steps": steps
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
			'echo "$SSH_PRIVATE_KEY" > utils/.ssh_private_key',
			"chmod 600 utils/.ssh_private_key"
		 ],
		"environment": environment_vars
	})
	
	# step 2: run pipeline
	for protocol in protocols:
		steps.append({
			"name": "setup_{}".format(protocol),
			"image": "registry.opviel.de:80/alpine_ansible:latest",
			"commands": [
				"export ANSIBLE_CONFIG=utils/ansible_drone.cfg",
				"/usr/bin/ansible-playbook utils/{}_setup.yaml".format(protocol)
			],
			"depends_on": ["export_ssh_key"]
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
