#/usr/bin/python3

class FilterModule(object):
    def filters(self):
        return {
            'format_userpass_output': self.format_userpass_output
        }

    def format_userpass_output(self, htpasswd_dict, hostname):
        msg = []
        msg.append("##################################################################")
        msg.append("###################  CHANGED USERS - HTPASSWD  ###################")
        for user in htpasswd_dict.keys():
            msg.append(f"{user}: {htpasswd_dict[user]} [LINK: http://{hostname}:80/{user}/index.html]")
        msg.append("##################################################################")
        return '\n'.join(msg)
