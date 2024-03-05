def main(ctx):

	protocols = [
		'xray',
		'hysteria',
		'ocserv',
		'sshvpn'
	]
	pipelines = [pipeline_1(), pipeline_2(protocols)]
	return pipelines

def pipeline_1():
	steps = []

	# step 1: check if image exists on remote registry
	remote_image = 'https://registry.opviel.de:80/library/alpine_ansible/latest'
	steps.append({
		"name": "check_image",
		"image": "alpine:latest",
		"commands": [
			'busybox wget -S --spider {} && echo -n "\nBUILD SKIPPED" && exit 0'.format(remote_image)
		]
	})

	# step 2: if doesn't exist, build and publish image to registry
	steps.append({
		"name": "publish_on_registry",
		"depends_on": ["check_image"],
		"image": "plugins/docker",
		"settings": {
			"repo": "registry.opviel.de/alpine_ansible",
			"dockerfile": "utils/Dockerfile",
			"registry": "registry.opviel.de",
			"insecure": "true",
			"purge": "true",
			"compress": "true",
			"context": "./utils",
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
		"ANSIBLE_CONFIG": "utils/ansible_drone.cfg",
		"SSH_PRIVATE_KEY": {
			"from_secret": "ssh_key"
		}
	}

	steps = []

	# step 1: export ssh private key to file
	steps.append({
		"name": "export_ssh_key",
		"image": "alpine",
		"commands": ["echo $SSH_PRIVATE_KEY > utils/.ssh_private_key"]
	})
	
	# step 2: run pipeline
	for protocol in protocols:
		steps.append({
			"name": "setup_{}".format(protocol),
			"image": "alpine_ansible",
			"commands": ["ansible-playbook utils/{}_setup.yaml".format(protocol)],
			"depends_on": ["export_ssh_key"]
		})

	return {
		"kind": "pipeline",
		"type": "docker",
		"name": "Execute Playbook",
		"platform": { "arch": "arm64" },
		"environments": environment_vars,
		"steps": steps
	}
