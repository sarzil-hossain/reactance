# Reactance - User Manual
Censorship resistant VPN automation and user management for servers and cloud services that is scalable.

## Table of Contents
  - [Goals](#goals)
  - [Protocols](#protocols)
  - [To Do](#to-do)
  - [Server Definitions](#server-definitions)
  - [User Definitions](#user-definitions)
  - [Playbook Execution](#playbook-execution)

### Goals
- Automatically sets up a wide range of up-to-date secure VPN protocols
- Automated User Management
- Bypasses Censorship
- Easy to set up and manage

### Protocols:
Protocols are sorted on specific order. Protocols upper in the list are more preferable for usage.

|Protocol|Server|Authentication Method|Server Verification Method|
|Cisco AnyConnect|OpenConnect|Certificate|TBD|
|Trojan|Xray core|Password only|XTLS Vision|
|VLESS|Xray core|UUID|XTLS Vision|
|VMESS|Xray core|UUID|XTLS Vision|
|Hysteria v2|Hysteria v2|Username & Password, Obfuscation|TBD|

### TO DO
Read [CONTRIBUTING.md](./CONTRIBUTING.md)

### Server Definitions
Servers are defined in inventory.yaml file. There are different groups for different protocols.
Example: The following config will setup all vpn servers on box1, only trojan on box2 and box4, and only ocserv on box3

```ini
[all_vpns]
box1

[trojan]
box2
box4

[ocserv]
box3
```
Supported groups: `all_vpns`, `vless`, `vmess`, `trojan`, `sshvpn`, `hysteria`, `ocserv`

### User Definitions
Users are defined as group variables. Please read the [README.md](group_vars/README.md) file in group_vars directory.

### Playbook Execution
To execute the playbook, simply run `ansible-playbook reactance_setup.yaml`. Include `--ask-become-pass` flag if you need to input your password.
