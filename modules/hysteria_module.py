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

def hysteria_user_control(ACTION, CLIENT_EMAIL, module):
    HYSTERIA_CONFIG_PATH = "/var/vms/hysteria/etc/config.json"
    
    with open(HYSTERIA_CONFIG_PATH, "r") as f:
        hysteria_config_dict = json.loads(f.read())
    
    if ACTION == "add":
        password = exec_shell("openssl rand -base64 32")
        user_dicts = hysteria_config_dict["auth"]["userpass"]
        if CLIENT_EMAIL in user_dicts.keys():
            raise Exception("ERROR: User %s already exists" %CLIENT_EMAIL) 
        hysteria_config_dict["auth"]["userpass"][CLIENT_EMAIL] = password
    if ACTION == "force_add":
        password = exec_shell("openssl rand -base64 32")
        hysteria_config_dict["auth"]["userpass"][CLIENT_EMAIL] = password
    if ACTION == "remove":
        hysteria_config_dict["auth"]["userpass"].pop(CLIENT_EMAIL)

    with open(HYSTERIA_CONFIG_PATH, "w") as f:
        f.write(json.dumps(hysteria_config_dict, indent=1))
        
def run_module():
    module = AnsibleModule(
        argument_spec=dict(
            protocol = dict(type='str', required=True),
            email = dict(type='str', required=True),
            action = dict(type='str', required=True)
        ),
        supports_check_mode=True
    )

    PROTO = module.params["protocol"]
    ACTION = module.params["action"]
    CLIENT_EMAIL = module.params["email"]

    hysteria_user_control()

def main():
    run_module()
