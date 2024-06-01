FROM alpine:latest

RUN apk add --no-cache  python3 py3-pip openssh-client
RUN pip3 install ansible netaddr hugo

CMD ["ansible-playbook", "--version"]
