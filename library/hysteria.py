from __future__ import absolute_import, division, print_function
__metaclass__ = type

import json
import shlex

XRAY_CONFIG_PATH = "/var/vpns/xray/etc/config.json"

HYSTERIA_CONFIG_FILE = "config.json"

def exec_shell(cmd, module):
    cmd_args = shlex.split(cmd)
    ran_cmd = module.run_command(cmd_args, environ_update={'TERM': 'dumb'})
    if ran_cmd.rc != 0:
        raise Exception(ran_cmd.stderr)
    return ran_cmd.stdout

def hysteria_get_users():
    with open(HYSTERIA_CONFIG_FILE, "r") as f:
        hysteria_config_dict = json.loads(f.read())
        previous_users = hysteria_config_dict["auth"]["userpass"]
    return previous_users, hysteria_config_dict

def hysteria_update_users(update_password):
    previous_users, hysteria_config_dict = hysteria_get_users()
    updated_users = set(update_password.keys())
    selected_users = set(updated_users)
    new_users_dict = {}
    for user in previous_users:
        if user in selected_users and not update_password[user]:
            new_users_dict[user] = previous_users[user]
    for user in selected_users:
        if user not in previous_users or update_password[user]:
            new_users_dict[user] = exec_shell("openssl rand -base64 32")
    with open("hysteria.json", "w") as f:
        hysteria_config_dict["auth"]["userpass"] = new_users_dict
        f.write(json.dumps(hysteria_config_dict, indent=1))

def run_module():
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
            update_password[user['name']] = True
        else:
            update_password[user['name']] = False

    ocserv_user_control(update_password)

def main():
    run_module()

if __name__ == "__main__":
    main()
