# Project VPN - User Manual
VPN Setup automation for bypassing government censorship

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
1. OpenConnect AnyConnect (ocserv) + Self Signed TLS Cert
2. Trojan + XTLS Vision
3. VLESS + XTLS Vision
4. VMESS + XTLS Vision
5. SSH VPN
6. Hysteria + Self Signed TLS Cert

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
To execute the playbook, simply run `ansible-playbook --become-method=doas --become -i inventory.ini project_vpns_setup.yaml`. Include `--ask-become-pass` flag if you need to input your password.
