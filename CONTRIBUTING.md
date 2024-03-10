# Reactance - Developer Manual

## Table of Contents
- [The Idea](#the-idea)
- [Developer Setup](#developer-setup)
- [Overall Structure](#overall-structure)
- [To Do](#todo)

## The Idea
Reactance is a collection of ansible roles that would setup numerous VPN protocols on your server. At the moment, you can do single server setup. But in future, support for multiple servers with a centralized database would be added.

## Developer Setup
You need `python3` installed. Make a virtual environment and install ansible in it `python3 -m venv .venv && source .venv/bin/activate pip3 install ansible`

## Overall Structure
There are different roles for different protocols. Each role does 3 things:
- Installing and running the VPN service in a chrooted environment
- Configuring the VPN service (configuration, writing certs and key files)
- User management for the VPN service (add, remove, expire users)

Installation and Configuration are done through ansible roles. The user management bit is accomplished through writing custom ansible modules that can be found in the `libraries` directory. Please refer to [Custom Modules README.md](library/README.md) to learn how to write custom modules for your protocol.

Each user can also be automatically removed after a specific time, which can be setup by adding `expires: yyyy-mm-dd` parameter in group_vars/all.yaml. Since some of these protocols do not have built in support for automatically expiring user access, this task is accomplished by running a python script on a daily basis as a cronjob. For each protocol, necessary functions are added in `roles/base/templates/user_expiry_control.py.j2`

## To-Do
- [X] single server support
- [x] user expiry support
- [ ] cleaning up and refactoring entire codebase
- [ ] multiple server support
