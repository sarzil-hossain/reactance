#!/usr/local/bin/python3 

from __future__ import absolute_import, division, print_function
__metaclass__ = type

from ansible.module_utils.basic import AnsibleModule
import json, os
import shlex

SSH_ROOT = "/var/vpns/sshvpn/.ssh"
AUTHORIZED_KEYS = os.path.join(SSH_ROOT, "authorized_keys")

def exec_shell(cmd, module):
    cmd_args = shlex.split(cmd)
    ran_cmd = module.run_command(cmd_args, environ_update={'TERM': 'dumb'})
    if ran_cmd.rc != 0:
        raise Exception(ran_cmd.stderr)
    return ran_cmd.stdout

def sshvpn_get_users():
    ssh_dir = os.path.join(os.getcwd(), SSH_ROOT)
    previous_users = [".".join(i.split('.')[:-1]) for i in os.listdir(ssh_dir) if i.endswith(".pub")]
    return previous_users

def sshvpn_update_users(update_password, module):
    previous_users = sshvpn_get_users()
    new_users = {}
    for user in update_password.keys():
        if user in previous_users and not update_password[user]:
            pass
        exec_shell(f"ssh-keygen -t rsa -b 4096 -C {user} -N '' -f '{user}'", module)
    with open(AUTHORIZED_KEYS, "w") as f:
        for user_key in new_users.keys():
            with open(os.path.join(SSH_ROOT, user_key + ".pub"), "r") as f_pub:
                f.write(f_pub.read())

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
    sshvpn_update_users(update_password, module)

def main():
    run_module()

if __name__ == "__main__":
    main()
