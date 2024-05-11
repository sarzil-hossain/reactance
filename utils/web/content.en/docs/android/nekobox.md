---
title: "Nekobox"
weight: 1
# bookFlatSection: false
# bookToc: true
# bookHidden: false
# bookCollapseSection: false
# bookComments: false
# bookSearchExclude: false
---



## Credentials 
{% if user.trojan is defined %}
Trojan URL: `trojan://{{ xray_user.trojan }}@{{ ansible_all_ipv4_addresses[0] }}:{{ vrojan_port|default(4436)}}?security=reality&sni={{reality_sni|default('behindthename.com')}}&fp=chrome&type=tcp&pbk={{ xray_public_key }}#trojan_{{ xray_user.key }}_{{ ansible_all_ipv4_addresses[0] }}`
{% endif %}

{% if user.vless is defined %}
VLESS URL: `vless://{{ xray_user.vless }}@{{ ansible_all_ipv4_addresses[0] }}:{{ vless_port|default(4437)}}?security=reality&sni={{reality_sni|default('behindthename.com')}}&fp=chrome&flow=xtls-rprx-vision&type=tcp&pbk={{ xray_public_key }}#vless_{{ xray_user.key }}_{{ ansible_all_ipv4_addresses[0] }}`
{% endif %}

{% if user.vmess is defined %}
VMESS URL: VLESS URL: `vmess://{{ xray_user.vmess }}@{{ ansible_all_ipv4_addresses[0] }}:{{ vmess_port|default(4438)}}?security=reality&sni={{reality_sni|default('behindthename.com')}}&fp=chrome&flow=xtls-rprx-vision&type=tcp&pbk={{ xray_public_key }}#vmess_{{ xray_user.key }}_{{ ansible_all_ipv4_addresses[0] }}`
{% endif %}
