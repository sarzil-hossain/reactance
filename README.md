# Reactance - User Manual
Censorship resistant scalable VPN/Proxy automation for OpenBSD with user management for servers and cloud services.

Supported OpenBSD versions: 7.4 (Tested)
Note: Please do not try to set up the automation on OpenBSD 7.5 as the xray server would fail because of x/sys library in golang. Check out [this issue on github](https://github.com/golang/go/issues/36435) for more info. Until the issue is resolved, the Xray server will not work on OpenBSD 7.5 .

## Table of Contents
  - [Description](#description)
  - [Protocols](#protocols)
  - [Server Definitions](#server-definitions)
  - [User Definitions](#user-definitions)
  - [Playbook Execution](#playbook-execution)
  - [Client Website](#client-website)
  - [Reading Logs](#reading-logs)
  - [CI/CD Pipelines](#cicd-pipelines)
  - [Contributing](#contributing)

## Description
Reactance is a complete automation to handle installation, user management, credential distribution of censorship-resistant VPN protocols on your openbsd server/cloud service(s) of choice. The server configuration is done through setting inventory variables. User configuration is done through using host and group variables. Read [Server Definitions](#server-definitions) and [User Definitions](#user-definitions) for more info.

Reactance builds websites for users/clients to view documentations and credentials. The htpasswd credential and URL of the website is showed at the end of `web` role at the end of reactance run.

It is also possible to test and deploy the VPN automation through using CI/CD pipelines. Please read [CI/CD Pipelines](#cicd-pipelines) for more info.

The goals of this project are:
- Automatically setting up a wide range of up-to-date secure VPN services  on OpenBSD
- Automated User Management and Expiration
- Bypassing Censorship
- Easy to set up and manage

## Protocols
These are the protocols currently supported by Reactance. Protocols upper in the list are more preferable for usage because of security and performance.

**NOTE: Hysteria2 is disabled by default. Because the sing-box clients available on the different platforms do not have any mechanism for verifying the proxy server's identity thus there's possibility of MITM attacks. Even if you include Hysteria in your configuration, it would be ignored**

|Protocol|Service|Authentication Method|Server Verification Method|Auto DNS Proxying|
|--|--|--|--|--|
|Cisco AnyConnect|OpenConnect|Certificate|TBD|Yes|
|Trojan|Xray core|Password only|XTLS Vision|Yes|
|VLESS|Xray core|UUID|XTLS Vision|Yes|
|VMESS|Xray core|UUID|XTLS Vision|Yes|
|SOCKS|SSH|private key|matching keypairs|No|
|Hysteria v2|Hysteria v2|Username & Password, Obfuscation|TBD|No|

## Server Definitions
Servers are defined in inventory.yaml file. There are different groups for different services.
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
|ocserv_port|port number for openconnect server|4430|all_vpns, ocserv|
|hysteria_port|port number for hysteria|4435|all_vpns, hysteria|
|trojan_port|port number for trojan|4436|all_vpns, xray|
|vless_port|port number for vless|4437|all_vpns, xray|
|vmess_port|port number for vmess|4438|all_vpns, xray|
|disable_webui|disable web interface for clients|false|all|
|disable_dns|disable dns and adblock setup|false|all|

## User Definitions
Users can be set up based on protocol (same users across all servers for same services) or hosts (specific users on specific servers). For user management based on services, write your user definitions in `group_vars/all.yaml`. For user management based on specific hosts, write your user definitions in `host_vars/all.yaml` (group_vars would be overriden for that host).

The parameters for the user definitions are:
|Parameter Name|Description|Type|Default Value|Importance|
|--|--|--|--|--|
|user|username|string|None|required|
|regen|overwrite existing password|boolean|false|optional|
|expire|user expiration date (format: yyyy-mm-dd)|string|None|optional|

Supported user lists are: `all_users`, `sshvpn_users`, `vless_users`, `vmess_users`, `trojan_users`, `hysteria_users`, `ocserv_users`

### Configuration Example
```yaml
# users set in all_users would be set up for every service
all_users:
    - user: foo
    - user: bar
vless_users:
    - user: baz
      regen: true # will regenerate password
      expires: 2025-10-13 # will remove user after yyyy-mm-dd
```

## Playbook Execution
It's recommended to run the playbook through a DroneCI pipeline. However if you wish to run it locally from your computer, run the following commands:

Step 1: At first, install the dependencies
```sh
apt install rsync # or whatever your package manager is
python3 -m venv .venv
source .venv/bin/activate
pip3 install ansible netaddr
git submodule add -f https://github.com/alex-shpak/hugo-book web/themes/hugo-book
```

Step 2: Generate a ssh key for the remote `root` user and store the private key as `reactance/.ssh_private_key`

Step 3: To execute the playbook, simply run
```sh
ansible-playbook reactance.yaml
```

## Client Website
The clients can retrieve the VPN credentials and read the docs from the client site that they can access from `http://x.x.x.x/client_name/index.html`. htpasswd based authentication is for authenticating the clients on the sites. The htpasswd credentials along with the URLs are shown at the end of reactance run (web role) or at the end of `setup_web` task in DroneCI.
The VPN credentials can be retrieved and the docs can be read from the client website. Please read [CONTRIBUTING.md](./CONTRIBUTING.md) to know how to update the site.

## Reading Logs
How to debug and fix errors with VPN services
1. Reading logs

|Protocol|Log File|
|--|--|
|ocserv|/var/reactance/ocserv/ocserv.log|
|hysteria|/var/reactance/hysteria/hysteria.log|
|xray|/var/reactance/xray/logs/{xray_access.log, xray_error.log}|
|sshvpn|/var/log/authlog|

2. Reading system calls: You can use `ktrace` and `kdump` to read system calls of processes to see if any errors appear.

## CI/CD pipeline
You can test and deploy vpn services on your server using CI/CD pipelines. As of now, only DroneCI is supported because of its simplicity, flexibility and ease of use. A `utils` folder can be found that contains a Dockerfile and drone starlark configuration for running the drone pipeline. Starlark is used instead of YAML, to make it easier to add/remove services.
You need to set the drone config path to `utils/drone.star` in the webui and also store the ssh key as a drone secret in `ssh_private_key` variable.

## Contributing
To contribute to the project, please refer to [CONTRIBUTING.md](./CONTRIBUTING.md)
