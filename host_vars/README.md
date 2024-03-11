# Setting up users
User names specific to specific hosts need be to be defined in `<host>.yaml`, where `<host>` is the ansible hostname.
## Table of Contents
- [Parameters](#parameters)
- [Configuration Example](#configuration-example)

## Parameters
The parameters for the user lists are:
|Parameter Name|Description|Type|Default Value|Importance|
|--|--|--|--|--|
|user|username|string|None|required|
|regen_pass|overwrite existing password|boolean|false|optional|
|expire|user expiry date|string|None|optional|

Supported user lists are: `all_users`, `sshvpn_users`, `vless_users`, `vmess_users`, `trojan_users`, `hysteria_users`, `ocserv_users`

## Configuration Example
box1.yaml
```yaml
# hysteria users for box1
hysteria_users:
    - user: deez
      regen_pass: true # will regenerate password
    - user: nuts
      expires: 2020-10-13 # will remove user after yyyy-mm-dd
```
