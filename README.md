# Reactance - User Manual
Censorship resistant scalable VPN automation with user management for servers and cloud services (WIP).

## Table of Contents
  - [Goals](#goals)
  - [Protocols](#protocols)
  - [Server Definitions](#server-definitions)
  - [User Definitions](#user-definitions)
  - [Playbook Execution](#playbook-execution)
  - [Retrieving Credentials](#retrieving-credentials)
  - [Reading Logs](#reading-logs)
  - [Contributing](#contributing)

## Goals
- Automatically sets up a wide range of up-to-date secure VPN protocols
- Automated User Management and Expiry
- Bypasses Censorship
- Easy to set up and manage
- Easy to 

## Protocols
Protocols are sorted on specific order. Protocols upper in the list are more preferable for usage.

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
Users are defined as group variables in `group_vars/all.yaml`. Please refer to [README.md](group_vars/README.md) file in group_vars directory.

## Playbook Execution
To execute the playbook, simply run `ansible-playbook reactance_setup.yaml`. Include `--ask-become-pass` flag if you need to input your password.

## Retrieving Credentials
The credentials for each protocols are shown at the end of drone run.

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
## Contributing
To contribute to the project, please refer to [CONTRIBUTING.md](./CONTRIBUTING.md)
