# Custom Modules
## Table of Contents
  - [Description](#description)
  - [Protocols](#protocols)
      - [ocserv.py](#ocserv.py)
	  - [xray.py](#xray.py)
      - [sshvpn.py](#sshvpn.py)
      - [hysteria.py](#hysteria.py)

## Description
Custom modules for user management for different protcols  

 ## Protocols
### xray.py
Description: User management module for xray (vless, vmess, trojan)
Input Parameters:
- users - all_users + vless_users/vmess_users/trojan_users
- protocol - vless/vmess/trojan

### ocserv.py
Description: User management module for ocserv
Input Parameters:
- users - all_users + ocserv_users

### hysteria.py
Description: User management module for hysteria
Input Parameters:
- users - all_users + hysteria_users

### sshvpn.py
Description: USer management module for sshvpn
Input Parameters:
- users - all_users + sshvpn_users
