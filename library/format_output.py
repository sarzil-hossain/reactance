#!/usr/local/bin/python3

from __future__ import absolute_import, division, print_function
__metaclass__ = type

from ansible.module_utils.basic import AnsibleModule
import json, shlex, os
from datetime import datetime

EXPIRE_USER_JSON_PATH = "/var/vpns/.user_expiration.json"
        
def run_module():
    changed = False
    module = AnsibleModule(
        argument_spec=dict(
            users = dict(type='list', required=True)
        ),
        supports_check_mode=True
    )

    user_pass_list = module.params["users"]
    msg = """
#########################
####  CHANGED USERS  ####
    """
    for protocol in user_pass_list:
        msg += f"## {protocol.key}"
        proto_user_pass_dict = protocol.values()
        for user in proto_user_pass_dict.keys():
            msg += f"# {user}: {proto_user_pass_dict[user]}"

    msg += "#########################"
    module.exit_json(changed=changed, msg=msg)

def main():
    run_module()

if __name__ == "__main__":
    main()
