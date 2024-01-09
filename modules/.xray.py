#!/bin/python3

import json
import subprocess

def exec_shell(cmd):
    cmd_ran = subprocess.run(cmd, shell=True, capture_output=True)
    if cmd_ran.stdout:
        raise Exception("ERROR: %s" %cmd_ran.stderr)
    return cmd_ran.stdout

def get_xray_users():
    XRAY_CONFIG_PATH = "config.json"
    with open(XRAY_CONFIG_PATH, "r") as f:
        xray_config_dict = json.loads(f.read())
    inbounds = xray_config_dict["inbounds"]
    protos_users = {}
    for inbound in inbounds:
        if inbound['protocol'] not in ['dokodemo-door']:
            protos_users[inbound['protocol']] = [j['email'] for j in inbound['settings']['clients']]
    return protos_users, xray_config_dict

def xray_update_users(update_password):
    previous_users, xray_config_dict = get_xray_users()

    for i, inbound in enumerate(xray_config_dict['inbounds']):
        if inbound['protocol'] in ['vless', 'vmess', 'trojan']:
            PROTO = inbound['protocol']
            previous_users_dict = inbound['settings']['clients']
            previous_users = [i['email'] for i in previous_users_dict]
            updated_users = set(update_password.keys())
            selected_users = set([i for i in previous_users if i in updated_users]).union(updated_users)
            new_users_list = []
            for user in selected_users:
                if user not in previous_users or update_password[user]:
                    new_user = { 'user': user, 'password': exec_shell("openssl rand -base64 32") }
                else:
                    new_user = { 'user': user, 'password': # get previous password}
                if PROTO in ["vless", "vmess"]:
                    new_user["flow"] = "xtls-rprx-vision"
                new_users_list.append(new_user)
            xray_config_dict['inbounds'][i]['settings']['clients'] = new_users_list

    with open(XRAY_CONFIG_PATH, "w") as f:
        f.write(json.dumps(xray_config_dict, indent=1))

def main():
    # CLIENTS = module.params["users"]
    update_password = {}
    xray_update_users(update_password)

    get_xray_users()


if __name__ == "__main__":
    main()
