from __future__ import absolute_import, division, print_function
__metaclass__ = type

import json
import shlex

def exec_shell(cmd, module):
    cmd_args = shlex.split(cmd)
    ran_cmd = module.run_command(cmd_args, environ_update={'TERM': 'dumb'})
    if rc != 0:
        raise Exception(ran_cmd.stderr)
    return ran_cmd.stdout


def ocserv_check_users(CLIENT_EMAIL):

    # get current users in list

    # get passed users list



def ocserv_user_control(ACTION, CLIENT_EMAIL):
    OCSERV_CONFIG_PATH = "/var/vms/ocserv/ocserv.passwd"

    with open(OCSERV_CONFIG_PATH, "r") as f:
        ocserv_content = f.read()

    ocserv_config_dict = dict(map(lambda x: x.split(':*:'), list(filter(lambda x: x != '', ocserv_content.split("\n")))))
    if ACTION == "add":
        password = exec_shell("openssl rand -base64 32")
        if CLIENT_EMAIL in ocserv_config_dict.keys():
            raise Exception("ERROR: User %s already exists" %CLIENT_EMAIL)
        ocserv_config_dict[CLIENT_EMAIL] = password
    if ACTION == "force_add":
        password = exec_shell("openssl rand -base64 32")
        ocserv_config_dict[CLIENT_EMAIL] = password
    if ACTION == "remove":
        ocserv_config_dict.pop(CLIENT_EMAIL)

    print(ocserv_config_dict)

    with open(OCSERV_CONFIG_PATH, "w") as f:
        f.write('\n'.join(list(map(lambda x: f"{x}:*:{ocserv_config_dict[x]}",ocserv_config_dict))))

        
def run_module():
    module = AnsibleModule(
        argument_spec=dict(
            protocol = dict(type='str', required=True),
            emails = dict(type='str', required=True),
            action = dict(type='str', required=True)
        ),
        supports_check_mode=True
    )

    CLIENT_EMAILS = module.params["email"]
    CLIENT_EMAILS = list(filter(lambda x: x != "", emails.split(" ")))
    for CLIENT_EMAIL in CLIENT_EMAILS:
        ocserv_user_control(PROTO, ACTION, CLIENT_EMAIL, module)

def main():
    run_module()
