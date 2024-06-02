#!/usr/local/bin/python3

from __future__ import absolute_import, division, print_function
__metaclass__ = type

from ansible.module_utils.basic import AnsibleModule
import json, shlex, os
from datetime import datetime


OCSERV_CERTS_DIR = "/var/reactance/ocserv/certs"

def exec_shell(cmd, module):
    rc, stdout, stderr= module.run_command(cmd, environ_update={'TERM': 'dumb'}, use_unsafe_shell=True)
    if rc != 0:
        module.fail_json(stderr)
    return stdout.rstrip()

def ocserv_get_users():
    previous_users = [".".join(i.split('.')[:-1]) for i in os.listdir(OCSERV_CERTS_DIR) if i.endswith(".p12")]
    return previous_users

def ocserv_user_control(update_password, module):
    previous_users = ocserv_get_users()
    selected_users = set(update_password.keys())
    new_users_dict = {}
    
    # Remove users not in group_vars
    for user in previous_users:
        if user not in selected_users or not update_password[user]:
            # new code goes here - remove user, update crl
            exec_shell(f"cat {OCSERV_CERTS_DIR}/{user}-cert.pem > {OCSERV_CERTS_DIR}/revoked.pem", module)
            exec_shell(f"certtool --generate-crl --load-ca-privkey {OCSERV_CERTS_DIR}/ca-key.pem --load-ca-certificate {OCSERV_CERTS_DIR}/ca-cert.pem --load-certificate {OCSERV_CERTS_DIR}/revoked.pem --template {OCSERV_CERTS_DIR}/crl.tmpl --outfile {OCSERV_CERTS_DIR}/crl.pem", module)
            exec_shell(f"rm {OCSERV_CERTS_DIR}/{user}-cert.pem {OCSERV_CERTS_DIR}/{user}-key.pem {OCSERV_CERTS_DIR}/{user}.p12", module)

    # Add new users or update password of existing users
    for user in selected_users:
        if user not in previous_users or update_password[user]:
            # new code goes here - generate template, certs
            user_template_contents = f"""
dn = "cn={user},UID={user}"
expiration_days = -1
signing_key
tls_www_client
            """
            user_template_file = os.path.join(OCSERV_CERTS_DIR, f"{user}.tmpl")
            with open(user_template_file, "w") as f:
                f.write(user_template_contents)
            exec_shell(f"certtool --generate-privkey --outfile {OCSERV_CERTS_DIR}/{user}-key.pem", module)
            exec_shell(f"certtool --generate-certificate --load-privkey {OCSERV_CERTS_DIR}/{user}-key.pem --load-ca-certificate {OCSERV_CERTS_DIR}/ca-cert.pem --load-ca-privkey {OCSERV_CERTS_DIR}/ca-key.pem --template {OCSERV_CERTS_DIR}/{user}.tmpl --outfile {OCSERV_CERTS_DIR}/{user}-cert.pem", module)
            exec_shell(f"certtool --to-p12 --load-privkey {OCSERV_CERTS_DIR}/{user}-key.pem --pkcs-cipher 3des-pkcs12 --load-certificate {OCSERV_CERTS_DIR}/{user}-cert.pem --outfile {OCSERV_CERTS_DIR}/{user}.p12 --password {user} --p12-name {user} --outder", module)
            exec_shell(f"rm {user_template_file}", module)
            new_users_dict[user] = {"ocserv": []} # a hack
            
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
        if 'regen' in user.keys() and user['regen']:
            update_password[user['user']] = True
        else:
            update_password[user['user']] = False

    new_users_dict = ocserv_user_control(update_password, module)
    module.exit_json(changed=True, msg=new_users_dict)

def main():
    run_module()

if __name__ == "__main__":
    main()
