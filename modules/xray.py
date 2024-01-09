#!/bin/python3

import json
import subprocess
XRAY_CONFIG_PATH = "config.json"

def exec_shell(cmd):
    cmd_ran = subprocess.run(cmd, shell=True, capture_output=True)
    if cmd_ran.stderr:
        raise Exception("ERROR: %s" %cmd_ran.stderr)
    return cmd_ran.stdout.decode()

def gen_password(protocol):
    return exec_shell({'xray': 'openssl rand -base64 32', 'vless': 'xray uuid', 'vmess': 'xray uuid'}[protocol])

def get_xray_users(protocol):
    with open(XRAY_CONFIG_PATH, "r") as f:
        xray_config_dict = json.loads(f.read())
    inbounds = xray_config_dict["inbounds"]
    protos_users = {}
    for inbound in inbounds:
        if inbound['protocol'] == protocol:
            protos_users[inbound['protocol']] = [j['email'] for j in inbound['settings']['clients']]
    return protos_users, xray_config_dict

def xray_update_users(update_password, protocol):
    previous_users, xray_config_dict = get_xray_users(protocol)

    # search through all inbound protocools
    for i, inbound in enumerate(xray_config_dict['inbounds']):
        if inbound['protocol'] == protocol:
            previous_users_dict = inbound['settings']['clients']
            previous_users = [i['email'] for i in previous_users_dict]
            updated_users = set(update_password.keys())
            selected_users = set(updated_users)
            new_users_list = []

            # keep old passwords
            for j, user in enumerate(previous_users):
                if user in selected_users and not update_password[user]:
                    login_method = {'vmess': 'id', 'vless': 'id', 'trojan': 'password'}[protocol]
                    new_user = { 'email': user, 'password': inbound['settings']['clients'][j][login_method] }
                    if protocol in ["vless", "vmess"]:
                        new_user["flow"] = "xtls-rprx-vision"
                    new_users_list.append(new_user)
                    
            # generate new passwords
            for user in selected_users:
                if user not in previous_users or update_password[user]:
                    login_method = {'vmess': 'id', 'vless': 'id', 'trojan': 'password'}[protocol]
                    new_user = { 'email': user, login_method: gen_password(protocol) }
                    if protocol in ["vless", "vmess"]:
                        new_user["flow"] = "xtls-rprx-vision"
                    new_users_list.append(new_user)
            xray_config_dict['inbounds'][i]['settings']['clients'] = new_users_list

    with open("file.json", "w") as f:
        f.write(json.dumps(xray_config_dict, indent=1))


def main():
    # CLIENTS = module.params["users"]
    users = [{'name': "ungabunga", 'regen_pass': True}, {'name': 'comrademp'}]
    update_password = {}
    for user in users:
        if 'regen_pass' in user.keys() and user['regen_pass']:
            update_password[user['name']] = True
        else:
            update_password[user['name']] = False

    print(users, update_password)
    exit()
    # {'a': True, 'b': False, 'comrademp': False}
    xray_update_users(update_password, protocol="vless")


if __name__ == "__main__":
    main()
