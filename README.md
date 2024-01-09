# Project VPN
__VPN Setup automation for bypassing government censorship_

### Goals
- Wide range of up-to-date secure VPN protocols
- Automated User Management
- Bypasses Censorship

### Protocols:
1. OpenConnect AnyConnect (ocserv) + Self Signed TLS Cert
2. Trojan + XTLS Vision
3. VLESS + XTLS Vision
4. VMESS + XTLS Vision
5. SSH VPN
6. Hysteria + Self Signed TLS Cert

### TO DO
 Testing the following protocols on all devices
- [X] xray protocols (vless, trojan, vmess with xtls-)
- [ ] Hysteria
- [X] ocserv 
- [ ] SSH

### Writing Ansible playbooks for
- [ ] xray
- [ ] ocserv
- [ ] sing-box
- [ ] ssh vpn

### VPN Server Definitions
All your servers are defined in the inventory.ini file
Example: The following config will setup all vpn servers on box1, only xray on box2 and box4, and only ocserv on box3

```ini
[all]
box1

[xray]
box2
box4

[ocserv]
box3
```

### Users Definitions
Users are defined as group variables in <protocol>.yaml files
Example: user1, user2 and user3 for all VPN servers, but user4 only for xray

```
all.yaml
users:
    - user1
    - user2
    - user3
      regen_pass: true
```
```
xray.yaml
users:
    - user4
```

### Playbook Execution
To execute the playbook, simply run `ansible-playbook --become-method=doas --become --ask-become-pass project_vpns_setup.yaml`
