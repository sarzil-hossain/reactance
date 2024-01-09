---
- name: "openbsd : setup xray"
  hosts: trojan
  become: true
  roles:
    - role: base
    - role: xray
