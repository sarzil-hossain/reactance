# Reactance - User Manual
Censorship resistant scalable VPN automation with user management for servers and cloud services (WIP) on OpenBSD.

## Table of Contents
  - [Description](#description)
  - [Protocols](#protocols)
  - [Server Definitions](#server-definitions)
  - [User Definitions](#user-definitions)
  - [Playbook Execution](#playbook-execution)
  - [Retrieving Credentials](#retrieving-credentials)
  - [Reading Logs](#reading-logs)
  - [CI/CD Pipelines](#cicd-pipelines)
  - [Contributing](#contributing)

## Description
Reactance is a complete automation to handle installation, user management, credential distribution of censorship-resistant VPN protocols on your openbsd server/cloud service(s) of choice. The server configuration is done through setting inventory variables. User configuration is done through using host and group variables. Read [Server Definitions](#server-definitions) and [User Definitions](#user-definitions) for more info.

It is also possible to test and deploy the VPN automation through using CI/CD pipelines. Please read [CI/CD Pipelines](#cicd-pipelines) for more info.

The goals of this project are:
- Automatically setting up up a wide range of up-to-date secure VPN protocols on OpenBSD
- Automated User Management and Expiry
- Bypassing Censorship
- Easy to set up and manage

## Protocols
These are the protocols currently supported by Reactance. Protocols upper in the list are more preferable for usage because of security and performance.

|Protocol|Server|Authentication Method|Server Verification Method|
|--|--|--|--|
|Cisco AnyConnect|OpenConnect|Certificate|TBD|
|Trojan|Xray core|Password only|XTLS Vision|
|VLESS|Xray core|UUID|XTLS Vision|
|VMESS|Xray core|UUID|XTLS Vision|
|Hysteria v2|Hysteria v2|Username & Password, Obfuscation|TBD|

## Server Definitions
Servers are defined in inventory.yaml file. There are different groups for different protocols.
Supported groups: `all_vpns`, `vless`, `vmess`, `trojan`, `sshvpn`, `hysteria`, `ocserv`

Example: The following config will setup all vpn servers on box1, only ocserv on box2 and box3

```json
all_vpns:
    hosts:
        box1:
            ansible_host: deez.example.com
            ansible_user: user1

ocserv:
    hosts:
        box2:
            ansible_host: nuts.example.com
            ansible_user: user2
            ocserv_network: "10.20.30.40/24"
        box3:
```
   
All variables:
|Name|Description|Default Value|Used Under|
|--|--|--|--|
|ocserv_network|network address for ocserv|172.16.16.1/24|all_vpns, ocserv|
|dns|dns resolver for ocserv|1.1.1.1|all_vpns, ocserv|
|ocserv_port|port number for openconnect server|4430|all_vpns, ocserv|
|hysteria_port|port number for hysteria|4435|all_vpns, hysteria|
|trojan_port|port number for trojan|4436|all_vpns, xray|
|vless_port|port number for vless|4437|all_vpns, xray|
|vmess_port|port number for vmess|4438|all_vpns, xray|

## User Definitions
Users can be set up based on protocol (same users across all servers for same services) or hosts (specific users on specific servers). For user management based on protocols, write your user definitions in `group_vars/all.yaml`. For user management based on specific hosts, write your user definitions in `host_vars/all.yaml` (group_vars would be overriden for that host).

The parameters for the user definitions are:
|Parameter Name|Description|Type|Default Value|Importance|
|--|--|--|--|--|
|user|username|string|None|required|
|regen_pass|overwrite existing password|boolean|false|optional|
|expire|user expiry date (format: yyyy-mm-dd)|string|None|optional|

Supported user lists are: `all_users`, `sshvpn_users`, `vless_users`, `vmess_users`, `trojan_users`, `hysteria_users`, `ocserv_users`

### Configuration Example
```yaml
# users set in all_users would be set up for every service
all_users:
    - user: foo
    - user: bar
vless_users:
    - user: baz
      regen_pass: true # will regenerate password
      expires: 2025-10-13 # will remove user after yyyy-mm-dd
```

## Playbook Execution
To execute the playbook, simply run `ansible-playbook reactance_setup.yaml`. Include `--ask-become-pass` flag if you need to input your password.

You can set up specific VPN services by using tags.
Supported tags: `vless`, `vmess`, `trojan`, `sshvpn`, `hysteria`, `ocserv`

## Retrieving Credentials
The credentials for each protocols are shown at the end of drone run. In future, connection packages would be added with a web UI for users to download credentials and use them.

## Reading Logs
How to debug and fix errors with VPN protocols
1. Reading logs

|Protocol|Log File|
|--|--|
|ocserv|/var/vpns/ocserv/ocserv.log|
|hysteria|/var/vpns/hysteria/hysteria.log|
|xray|/var/vpns/xray/logs/{xray_access.log, xray_error.log}|
|sshvpn|/var/log/authlog|

2. Reading system calls: You can use `ktrace` and `kdump` to read system calls of processes to see if any errors appear.

## CI/CD pipeline
You can test and deploy vpn services on your server using CI/CD pipelines. As of now, only DroneCI is supported because of its simplicity, flexibility and ease of use. A `utils` folder can be found that contains a Dockerfile and drone starlark configuration for running the drone pipeline. Starlark is used instead of YAML, to make it easier to add/remove protocols.
You need to set the drone config path to `utils/drone.star` in the webui and also store the ssh key as a drone secret in `ssh_private_key` variable.

## Contributing
To contribute to the project, please refer to [CONTRIBUTING.md](./CONTRIBUTING.md)
