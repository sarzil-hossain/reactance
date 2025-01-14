#!/usr/local/bin/python3

from __future__ import absolute_import, division, print_function
__metaclass__ = type

from ansible.module_utils.basic import AnsibleModule
import json, shlex, os
from datetime import datetime

XRAY_CONFIG_PATH = "/var/reactance/xray/etc/config.json"
VISION_PUBKEY_FILE = "/var/reactance/xray/public_key"

def exec_shell(cmd, module):
    rc, stdout, stderr = module.run_command(cmd, environ_update={'TERM': 'dumb'})
    if rc != 0:
        module.fail_json(stderr)
    return stdout.rstrip()
def xray_gen_password(protocol, module):
    login_method = {'vmess': 'id', 'vless': 'id', 'trojan': 'password'}[protocol]
    return login_method, exec_shell({'trojan': 'openssl rand -hex 32', 'vless': '/var/reactance/xray/bin/xray uuid', 'vmess': '/var/reactance/xray/bin/xray uuid'}[protocol], module)

def xray_get_users(protocol):
    with open(XRAY_CONFIG_PATH, "r") as f:
        xray_config_dict = json.loads(f.read())
    inbounds = xray_config_dict["inbounds"]
    protos_users = {}
    for inbound in inbounds:
        if inbound['protocol'] == protocol:
            protos_users[inbound['protocol']] = [j['email'] for j in inbound['settings']['clients']]
    return protos_users, xray_config_dict

def xray_user_control(update_password, protocol, address, service_port, public_key, module):
    previous_users, xray_config_dict = xray_get_users(protocol)
    user_pass_list = []
    all_users_dict = {}
    new_users_dict = {}

    # search through all inbound protocools
    for i, inbound in enumerate(xray_config_dict['inbounds']):
        if inbound['protocol'] == protocol:
            previous_users_dict = inbound['settings']['clients']
            previous_users_list = [i['email'] for i in previous_users_dict]
            selected_users = set(update_password.keys())

            # keep old passwords
            for user in previous_users_dict:
                if user['email'] in selected_users and not update_password[user['email']]:
                    user_pass_list.append(user)
                    all_users_dict[user['email']] = user[{'vmess': 'id', 'vless': 'id', 'trojan': 'password'}[protocol]]

            # generate new passwords
            for user in selected_users:
                if user not in all_users_dict.keys():
                    login_method, xray_password = xray_gen_password(protocol, module)
                    new_user = { 'email': user, login_method: xray_password }
                    xray_url = f"{protocol}://{ xray_password }@{ address }:{ service_port }?security=reality&sni=behindthename.com&fp=chrome&pbk={ public_key }"
                    all_users_dict[user] = {protocol: xray_password}
                    if protocol in ["vless", "vmess"]:
                        new_user["flow"] = "xtls-rprx-vision"
                        xray_url += "&flow=xtls-rprx-vision"
                    xray_url += f"#{protocol}_{user}"
                    user_pass_list.append(new_user)
                    new_users_dict[user] = {protocol: xray_url}
		
            xray_config_dict['inbounds'][i]['settings']['clients'] = user_pass_list

    with open(XRAY_CONFIG_PATH, "w") as f:
        f.write(json.dumps(xray_config_dict, indent=1))

    return new_users_dict

def run_module():
    module = AnsibleModule(
        argument_spec=dict(
            users = dict(type='list', required=True),
            protocol = dict(type='str', required=True),
	        address = dict(type='str', required=True),
            service_port = dict(type='int', required=True),
	        public_key = dict(type='str', required=True)
        ),
        supports_check_mode=True
    )

    users = module.params["users"]
    protocol = module.params["protocol"]
    address = module.params["address"]
    service_port = module.params["service_port"]
    public_key = module.params["public_key"]
    update_password = {}

    for user in users:
        if 'regen' in user.keys() and user['regen']:
            update_password[user['user']] = True
        else:
            update_password[user['user']] = False

    new_users_dict = xray_user_control(update_password, protocol, address, service_port, public_key, module)
    module.exit_json(changed=True, msg=new_users_dict)

def main():
    run_module()

if __name__ == "__main__":
    main()
