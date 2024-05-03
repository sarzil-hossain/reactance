# Reactance - Developer Manual

## Table of Contents
- [Description](#description)
- [Development Environment Setup](#development-environment-setup)
- [Developing Service Roles](#developing-service-roles)
- [Developing User Management Modules](#developing-user-management-modules)
- [Adding User Expiration Functionality](#adding-user-expiration-functionality)
- [To Do](#to-do)

## Description
Roles are used for installing, configuring services. Custom ansible modules are used for performing user management on servers. There are separate roles and user management modules for each protocol.

1. Installing, configuring and running the VPN service in a chrooted environment through roles
2. User management for the VPN service through custom modules and calling them inside roles
3. Adding user expiration support through custom python script ran on a daily cronjob

## Development Environment Setup
You need `python3` installed. Make a virtual environment and install ansible in it `python3 -m venv .venv && source .venv/bin/activate && pip3 install ansible`

## Developing Service Roles
Each role should have the following tasks:
1. `check_service_exists.yaml` - checks if the service is installed on server, if not, installation task is ran.
2. `install_service.yaml` - installs the service on the server in a chrooted environment
3. `configure_service.yaml` - generates server configuration file for the service
4. `create_users_service.yaml` - runs user management module
and necessary handlers to restart services, and other things required for the protocol

## Developing User Management Modules
For each protocol, you need to write a custom module for performing user management on servers.

1. input: each module takes a list of user definitions as input. The list is comprised of `all_users` and `service_users`
2. user management: the module would then run the necessary functions to perform the user management. For example, reading and updating configuration files or password files.
3. output: each module should return the list of username:password pairs as output or a message (as in sshvpn) in the following format:
```json
{ 
    "service name": {
        "user1": "password1",
        "user2": "password2"
    }
}
```

## Adding User Expiration Functionality
All services do not support automatic expiration of users, which is a very needed feature. Reactance however accomplishes that through running a python script as a daily cronjob. The user expiry control script is a part of the base role and templated out during ansible run. The [user_expiration_control.py script](roles/base/templates/user_expiration_control.py.j2) is stored in `roles/base/templates` directory. 

The user expiration information is stored in a json file that has the following format:
```json
{
    "date time in unix format": [
        "user_1",
        "user_2"
    ],
    "another date time in unix format": [
        "user_1",
        "user_3"
    ]
}

```
The unix date time is compared with current date, and if it's less than the current date time, the list of users associated to it is added to the list of users to remove. The list is then passed to functions that retrieve the list of previous users, remove users from provided list, saves the final list in configuration/password files.

## Client Website
At first, install hugo and git on your host machine. Hugo can be installed with `pip3 install hugo`. Follow your OS's documentations on installing git.

The base website is located in `utils/web`. For reactance, we are using a Hugo theme called `Book`. To add/modify contents of the pages, update the markdown files in `utils/web/content`. You can build the site locally by adding the theme as a submodule by running the following commands:

```sh
git submodule add https://github.com/alex-shpak/hugo-book themes/hugo-book utils/web/themes/hugo-book
hugo server # for testing
hugo # for building
```

Build site would be stored in `utils/web/public` directory. In production, the site would be built by Drone.

## To-Do
- [X] single server support
- [x] user expiration support
- [ ] adding connection packages
- [ ] adding webui for clients to download connection packages
- [ ] cleaning up and refactoring entire codebase
- [ ] multiple server support
