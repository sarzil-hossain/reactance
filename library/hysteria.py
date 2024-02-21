#!/usr/local/bin/python3

from __future__ import absolute_import, division, print_function
__metaclass__ = type

from ansible.module_utils.basic import AnsibleModule
import json, shlex, os
from datetime import datetime

HYSTERIA_CONFIG_FILE = "/var/vpns/hysteria/etc/config.json"

def exec_shell(cmd, module):
    rc, stdout, stderr= module.run_command(cmd, environ_update={'TERM': 'dumb'}, use_unsafe_shell=True)
    if rc != 0:
        module.fail_json(stderr)
    return stdout.rstrip()

def hysteria_get_users():
    with open(HYSTERIA_CONFIG_FILE, "r") as f:
        hysteria_config_dict = json.loads(f.read())
        previous_users = hysteria_config_dict["auth"]["userpass"]
    return previous_users, hysteria_config_dict

def hysteria_user_control(update_password, module):
    previous_users, hysteria_config_dict = hysteria_get_users()
    selected_users = set(update_password.keys())
    new_users_dict = {}
    for user in selected_users:
        if user in previous_users and not update_password[user]:
            new_users_dict[user] = previous_users[user]
        else:
            new_users_dict[user] = exec_shell("openssl rand -base64 32", module)
    with open(HYSTERIA_CONFIG_FILE, "w") as f:
        hysteria_config_dict["auth"]["userpass"] = new_users_dict
        f.write(json.dumps(hysteria_config_dict, indent=1))

    return new_users_dict

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

    user_pass_dict = hysteria_user_control(update_password, module)
    module.exit_json(changed=True, msg={"hysteria": user_pass_dict})

def main():
    run_module()

if __name__ == "__main__":
    main()
