#!/usr/local/bin/python3

from __future__ import absolute_import, division, print_function
__metaclass__ = type

from ansible.module_utils.basic import AnsibleModule
import json
import shlex

OCSERV_CONFIG_PATH = "/var/vpns/ocserv/ocserv.passwd"

def exec_shell(cmd, module):
    cmd_args = shlex.split(cmd)
    ran_cmd = module.run_command(cmd_args, environ_update={'TERM': 'dumb'})
    if ran_cmd.rc != 0:
        raise Exception(ran_cmd.stderr)
    return ran_cmd.stdout

def ocserv_gen_password():
    return exec_shell("openssl rand -base64 32")

def ocserv_get_users():
    with open(OCSERV_CONFIG_PATH, "r") as f:
        ocserv_content = f.read()

    ocserv_config_dict = dict(map(lambda x: x.split(':*:'), list(filter(lambda x: x != '', ocserv_content.split("\n")))))
    return ocserv_config_dict.keys(), ocserv_config_dict

def ocserv_user_control(update_password):
    previous_users, previous_user_password = ocserv_get_users()
    updated_users = set(update_password.keys())
    selected_users = set(updated_users)
    new_users_list = []
    for user in previous_users:
        if user in selected_users and not update_password[user]:
            new_users_list.append({'user': user, 'password': previous_user_password[user]})
    for user in selected_users:
        if user not in previous_users or update_password[user]:
            new_users_list.append({'user': user, 'password': ocserv_gen_password()})

    with open(OCSERV_CONFIG_PATH, "w") as f:
        f.write('\n'.join(list(map(lambda x: f"{x['user']}:*:{x['password']}", new_users_list))))
        
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

    ocserv_user_control(update_password)

def main():
    run_module()

if __name__ == "__main__":
    main()
