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
    rc, stdout, stderr= module.run_command(cmd_args, environ_update={'TERM': 'dumb'})
    if rc != 0:
        module.fail_json(stderr)
    return stdout

def sshvpn_get_users():
    previous_users = [".".join(i.split('.')[:-1]) for i in os.listdir(SSH_ROOT) if i.endswith(".pub")]
    return previous_users

def sshvpn_update_users(update_password, module):
    previous_users = sshvpn_get_users()
    all_users = set(previous_users)

    for user in update_password.keys():
        if user not in previous_users or update_password[user]:
            ssh_keygen_cmd = "ssh-keygen -t rsa -b 4096 -C {user} -N '' -f '{SSH_ROOT}/{user}'"
            exec_shell(f"[[ -f {SSH_ROOT}/{user} ]] && {ssh_keygen_cmd} <<<y || {ssh_keygen_cmd}", module)
            all_users.add(user)

    # Overwrite existing authorized_key file
    with open(AUTHORIZED_KEYS, "w") as f:
        for user in all_users:
            user_pubkey_file = os.path.join(SSH_ROOT, f"{user}.pub")
            with open(user_pubkey_file, "r") as pkey:
                f.write(pkey.read())

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
    module.exit_json(changed=True, msg=f"Retrieve keys from {SSH_ROOT}")

def main():
    run_module()

if __name__ == "__main__":
    main()
