---
title: "Openconnect"
weight: 1
# bookFlatSection: false
# bookToc: true
# bookHidden: false
# bookCollapseSection: false
# bookComments: false
# bookSearchExclude: false
---

Hello World

### Credentials

Here are the VPN credentials for connecting to the server:
Server: `{{ ansible_all_ipv4_addresses[0] }}`
Port: `{{ ocserv_port | default(4430) }}`

Client Key: [Click to download Client Key](/ocserv-user-key.pem)
Client Certificate: [Click to download Client Certificate](/ocserv-user-cert.pem)
Client P12 file: [Click to download client P12 file](/ocserv-user.p12)
Server Certificate: [Click to download Server Key](/server-cert.pem)

