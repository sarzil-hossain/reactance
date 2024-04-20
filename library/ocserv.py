#!/usr/local/bin/python3

from __future__ import absolute_import, division, print_function
__metaclass__ = type

from ansible.module_utils.basic import AnsibleModule
import json, shlex, os
from datetime import datetime

OCSERV_ROOT_DIR = "/var/vpns/ocserv"
OCSERV_CERTS_DIR = os.path.join(OCSERV_ROOT_DIR, "certs")

def exec_shell(cmd, module):
    rc, stdout, stderr= module.run_command(cmd, environ_update={'TERM': 'dumb'}, use_unsafe_shell=True)
    if rc != 0:
        module.fail_json(stderr)
    return stdout.rstrip()

def ocserv_get_users():
    previous_users = [".".join(i.split('.')[:-1]) for i in os.listdir(OCSERV_CERTS_DIR) if i.endswith(".pub") and not i.startswith(("server", "ca"))]
    return previous_users

def ocserv_user_control(update_password, module):
    previous_users = ocserv_get_users()
    selected_users = set(update_password.keys())

    # Remove users not in group_vars
    for user in previous_users:
        if user not in selected_users:
            # new code goes here - remove user, update crl
            exec_shell(f"cat { OCSERV_CERTS_DIR }/{user}-cert.pem >> { OCSERV_CERTS_DIR }/revoked.pem", module)
            exec_shell(f"certtool --generate-crl --load-ca-privkey { OCSERV_CERTS_DIR }/ca-key.pem --load-ca-certificate { OCSERV_CERTS_DIR }/ca-cert.pem --load-certificate { OCSERV_CERTS_DIR }/revoked.pem --template { OCSERV_CERTS_DIR }/crl.tmpl --outfile { OCSERV_CERTS_DIR }/crl.pem", module)
            exec_shell("rm {OCSERV_CERTS_DIR}/{user}-cert.pem {OCSERV_CERTS_DIR}/{user}-key.pem", module)
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
            user_template_file = os.path.join(OCSERV_CERTS_DIR, f"{user}.tmpl")
            with open(user_template_file, "w") as f:
                f.write(user_template_contents)
            exec_shell(f"certtool --generate-privkey --outfile { OCSERV_CERTS_DIR }/{user}-key.pem", module)
            exec_shell(f"certtool --generate-certificate --load-privkey { OCSERV_CERTS_DIR }/{user}-key.pem --load-ca-certificate { OCSERV_CERTS_DIR }/ca-cert.pem --load-ca-privkey { OCSERV_CERTS_DIR }/ca-key.pem --template { OCSERV_CERTS_DIR }/{user}.tmpl --outfile { OCSERV_CERTS_DIR }/{user}-cert.pem", module)
            exec_shell(f"rm {user_template_file}", module)
        
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

    ocserv_user_control(update_password, module)
    msg = {"ocserv":{"retrieve keys from": os.path.join(OCSERV_ROOT_DIR, "certs")}}
    module.exit_json(changed=True, msg=msg)

def main():
    run_module()

if __name__ == "__main__":
    main()
