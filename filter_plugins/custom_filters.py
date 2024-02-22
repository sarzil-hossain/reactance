#/usr/bin/python3

class FilterModule(object):
    def filters(self):
        return {
            'format_userpass_output': self.format_userpass_output
        }

    def format_userpass_output(self, user_pass_list):
        msg = []
        msg.append("##################################")
        msg.append("#########  CHANGED USERS  ########")
        for protocol in user_pass_list:
            msg.append(f"# {next(iter(protocol.keys()))}")
            iter_proto = iter(protocol.values())
            while (x := next(iter_proto, None)) != None:
                for y in x.keys():
                    msg.append(f" - {y}: {x[y]}")
        msg.append("##################################")
        return '\n'.join(msg)
