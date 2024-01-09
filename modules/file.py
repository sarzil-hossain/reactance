import json, subprocess

OCSERV_CONFIG_PATH = "ocserv.passwd"

def exec_shell(cmd):
    return subprocess.run(cmd, shell=True, capture_output=True).stdout.decode().strip()

def ocserv_gen_password():
    return exec_shell("openssl rand -base64 32")

def xray_get_users():
    with open(OCSERV_CONFIG_PATH, "r") as f:
        ocserv_content = f.read()

    ocserv_config_dict = dict(map(lambda x: x.split(':*:'), list(filter(lambda x: x != '', ocserv_content.split("\n")))))
    return ocserv_config_dict.keys(), ocserv_config_dict
 


def ocserv_user_control(update_password):
    previous_users, previous_user_password = xray_get_users()
    updated_users = set(update_password.keys())
    selected_users = set(updated_users)
    new_users_list = []
    for user in previous_users:
        if user in selected_users and not update_password[user]:
            new_users_list.append({'user': user, 'password': previous_user_password[user]})
    for user in selected_users:
        if user not in previous_users or update_password[user]:
            new_users_list.append({'user': user, 'password': ocserv_gen_password()})
    print(new_users_list)
    with open("ocserv.new.passwd", "w") as f:
        f.write('\n'.join(list(map(lambda x: f"{x['user']}:*:{x['password']}", new_users_list))))
        
def run_module():

    users = [{'name': 'a', 'regen_pass': True}, {'name': 'b'}, {'name': 'c'}]
    update_password = {}
    for user in users:
        if 'regen_pass' in user.keys() and user['regen_pass']:
            update_password[user['name']] = True
        else:
            update_password[user['name']] = False


    ocserv_user_control(update_password)

def main():
    run_module()

if __name__ == "__main__":
    main()
