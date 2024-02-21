#!/usr/local/bin/python3

from __future__ import absolute_import, division, print_function
__metaclass__ = type

from ansible.module_utils.basic import AnsibleModule
import json, shlex, os
from datetime import datetime

OCSERV_CONFIG_PATH = "/var/vpns/ocserv/ocserv.passwd"

def exec_shell(cmd, module):
    rc, stdout, stderr= module.run_command(cmd, environ_update={'TERM': 'dumb'}, use_unsafe_shell=True)
    if rc != 0:
        module.fail_json(stderr)
    return stdout.rstrip()

def ocserv_get_users():
    ocserv_config_dict = {}
    if os.path.isfile(OCSERV_CONFIG_PATH):
        with open(OCSERV_CONFIG_PATH, "r") as f:
            ocserv_content = f.read()
            ocserv_config_dict = dict(map(lambda x: x.split(':*:'), list(filter(lambda x: x != '', ocserv_content.split("\n")))))
    return ocserv_config_dict.keys(), ocserv_config_dict

def ocserv_user_control(update_password, module):
    previous_users, previous_user_password = ocserv_get_users()
    selected_users = set(update_password.keys())
    user_pass_dict = {}

    # Remove users not in group_vars
    for user in previous_users:
        if user not in selected_users:
            exec_shell(f"ocpasswd -d {user} -c {OCSERV_CONFIG_PATH}", module)

    # Add new users or update password of existing users
    for user in selected_users:
        if user not in previous_users or update_password[user]:
            ocserv_password = exec_shell("openssl rand -base64 32", module)
            exec_shell(f"echo '{ocserv_password}' | ocpasswd -c {OCSERV_CONFIG_PATH} {user}", module)
            user_pass_dict[user] = ocserv_password

    return user_pass_dict
        
def run_module():
    module = AnsibleModule(
        argument_spec=dict(
            users = dict(type='list', required=True)
        ),
        supports_check_mode=True
    )
    users = module.params["users"]
    update_password = {}

    for user in users:
        if 'regen_pass' in user.keys() and user['regen_pass']:
            update_password[user['user']] = True
        else:
            update_password[user['user']] = False

    user_pass_dict = ocserv_user_control(update_password, module)
    module.exit_json(changed=True, msg={"ocserv": user_pass_dict})

def main():
    run_module()

if __name__ == "__main__":
    main()
