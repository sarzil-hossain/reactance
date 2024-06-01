FROM alpine:latest

RUN apk add --no-cache ansible py3-netaddr
RUN apk add --no-cache --repository=https://dl-cdn.alpinelinux.org/alpine/edge/community hugo

CMD ["ansible-playbook", "--version"]
