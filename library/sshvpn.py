#!/usr/local/bin/python3 

from __future__ import absolute_import, division, print_function
__metaclass__ = type

from ansible.module_utils.basic import AnsibleModule
import json, shlex, os
from datetime import datetime

SSH_ROOT = "/home/sshvpn/.ssh"
AUTHORIZED_KEYS = os.path.join(SSH_ROOT, "authorized_keys")

def exec_shell(cmd, module):
    rc, stdout, stderr= module.run_command(cmd, environ_update={'TERM': 'dumb'}, use_unsafe_shell=True)
    if rc != 0:
        module.fail_json(stderr)
    return stdout.rstrip()

def sshvpn_get_users():
    previous_users = [".".join(i.split('.')[:-1]) for i in os.listdir(SSH_ROOT) if i.endswith(".pub")]
    return previous_users

def sshvpn_update_users(update_password, module):
    previous_users = sshvpn_get_users()

    # Remove users not in new group_vars
    for user in previous_users:
        if user not in update_password.keys():
            exec_shell(f"rm {user} {user}.pub", module)

    # Update keys for new users or regenerate keys for old users
    for user in update_password.keys():
        if user not in previous_users or update_password[user]:
            exec_shell(f"yes | ssh-keygen -q -t rsa -b 4096 -C {user} -N \'\' -f \'{SSH_ROOT}/{user}\'", module)

    # Overwrite existing authorized_key file
    users_pubkeys = [i for i in os.listdir(SSH_ROOT) if i.endswith(".pub")]
    with open(AUTHORIZED_KEYS, "w") as f:
        for user_pubkey in users_pubkeys:
            user_pubkey_file = os.path.join(SSH_ROOT, user_pubkey)
            with open(user_pubkey_file, "r") as pkey:
                f.write(pkey.read())

    # kill running sessions
    exec_shell(f"pkill -u sshvpn &>/dev/null", module)

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
        if 'regen' in user.keys() and user['regen']:
            update_password[user['user']] = True
        else:
            update_password[user['user']] = False

    sshvpn_update_users(update_password, module)
    msg = {"sshvpn":{"retrieve keys from": SSH_ROOT}}
    module.exit_json(changed=True, msg=msg)

def main():
    run_module()

if __name__ == "__main__":
    main()
