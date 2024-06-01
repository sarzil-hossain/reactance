#!/usr/local/bin/python3

from __future__ import absolute_import, division, print_function
__metaclass__ = type

from ansible.module_utils.basic import AnsibleModule
import json, shlex, os
from datetime import datetime

EXPIRE_USER_JSON_PATH = "/var/reactance/.user_expiration.json"

def run_module():
    changed = False
    module = AnsibleModule(
        argument_spec=dict(
            users = dict(type='list', required=True)
        ),
        supports_check_mode=True
    )

    users = module.params["users"]

    user_expire_dict = {}
    if os.path.exists(EXPIRE_USER_JSON_PATH):
        with open(EXPIRE_USER_JSON_PATH, 'r') as f:
            user_expire_dict = json.loads(f.read())

    for user in users:
        if 'expire' in user.keys():
            changed = True
            time = str(datetime(*[int(i) for i in user['expire'].split('-')]).timestamp())
            if time not in user_expire_dict.keys():
                user_expire_entry = set() # To make sure we don't have duplicates
            else:
                user_expire_entry = set(user_expire_dict[time])
            user_expire_entry.add(user['user'])
            user_expire_dict[time] = list(user_expire_entry) # JSON can't work with sets

    with open(EXPIRE_USER_JSON_PATH, 'w') as f:
        f.write(json.dumps(user_expire_dict, indent=1))
    
    module.exit_json(changed=changed)

def main():
    run_module()

if __name__ == "__main__":
    main()
