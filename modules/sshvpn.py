import os
import json
import subprocess

SSH_ROOT = "ssh_keys"

def exec_cmd(cmd):
    ran_cmd = subprocess.run(cmd, shell=True, capture_output=True)
    if ran_cmd.stderr:
        raise Exception(ran_cmd.stderr)
    return ran_cmd.stdout.decode().strip()

def hysteria_get_users():
    ssh_dir = os.path.join(os.getcwd(), SSH_ROOT)
    previous_users = [".".join(i.split('.')[:-1]) for i in os.listdir(ssh_dir) if i.endswith(".pub")]
    return previous_users

def hysteria_update_users(update_password):
    previous_users = hysteria_get_users()
    new_users = {}
    for user in update_password.keys():
        if user in previous_users and not update_password[user]:
            pass
        exec_cmd(f"ssh-keygen -t rsa -b 4096 -C {user} -N '' -f '{user}'")

def run_module():
    users = [{'name': 'hello', 'regen_pass': True}, {'name': 'comrademp'}, {'name': 'user'}]
    update_password = {}
    for user in users:
        if 'regen_pass' in user.keys() and user['regen_pass']:
            update_password[user['name']] = True
        else:
            update_password[user['name']] = False
    hysteria_update_users(update_password)

def main():
    run_module()

if __name__ == "__main__":
    main()
