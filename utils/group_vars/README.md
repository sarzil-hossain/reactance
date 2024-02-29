# Setting up users
User names need to be specified in all.yaml. Use the following format:

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

Supported user lists are: `all_users`, `sshvpn_users`, `vless_users`, `vmess_users`, `trojan_users`, `hysteria_users`, `ocserv_users`
