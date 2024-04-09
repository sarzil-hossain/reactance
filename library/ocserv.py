#!/usr/local/bin/python3

from __future__ import absolute_import, division, print_function
__metaclass__ = type

from ansible.module_utils.basic import AnsibleModule
import json, shlex, os
from datetime import datetime

OCSERV_CONFIG_PATH = "/var/vpns/ocserv/"
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

    # Remove users not in group_vars
    for user in previous_users:
        if user not in selected_users:
            # new code goes here - remove user, update crl
            exec_shell(f"cat /var/vpns/ocserv/certs/{user}-cert.pem >> /var/vpns/ocserv/certs/revoked.pem", module)
            exec_shell(f"certtool --generate-crl --load-ca-privkey /var/vpns/ocserv/certs/ca-key.pem --load-ca-certificate /var/vpns/ocserv/certs/ca-cert.pem --load-certificate /var/vpns/ocserv/certs/revoked.pem --template /var/vpns/ocserv/certs/crl.tmpl --outfile /var/vpns/ocserv/certs/crl.pem", module)
            exec_shell("rcctl reload ocserv", module)

    # Add new users or update password of existing users
    for user in selected_users:
        if user not in previous_users or update_password[user]:
            # new code goes here - generate template, certs
            user_template_contents = f"""
dn = "cn={user},UID={user}"
expiration_days = 3650
signing_key
tls_www_client
            """
            user_template_fpath = os.path.join(OCSERV_CONFIG_PATH, "certs", f"{user}.tmpl")
            with open(user_template_fpath, "w") as f:
                f.write(user_template_contents)
            exec_shell(f"certtool --generate-privkey --outfile /var/vpns/ocserv/certs/{user}-key.pem", module)
            exec_shell(f"certtool --generate-certificate --load-privkey /var/vpns/ocserv/certs/{user}-key.pem --load-ca-certificate /var/vpns/ocserv/certs/ca-cert.pem --load-ca-privkey /var/vpns/ocserv/certs/ca-key.pem --template /var/vpns/ocserv/certs/{user}.tmpl --outfile /var/vpns/ocserv/certs/{user}-cert.pem", module)
        
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

    ocserv_user_control(update_password, module)
    msg = {"ocserv":{"retrieve keys from": os.path.join(OCSERV_CONFIG_PATH, "certs")}}
    module.exit_json(changed=True, msg=msg)

def main():
    run_module()

if __name__ == "__main__":
    main()
