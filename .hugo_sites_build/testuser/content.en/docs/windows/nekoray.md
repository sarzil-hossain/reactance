---
title: NekoRay (V2Ray)
type: docs
---

# NekoRay

In this tutorial you will learn how to use NekoRay VPN client on Windows devices.

NekoRay is a VPN client supporting a variety of VPN protocols, and we will be using this handy client to use our main VPN protocols on desktop computers, including VLess, VMess, and Trojan.

## How to use NekoRay:

1. Go to NekoRay's GitHub page by clicking the button below. Click on the link that is highlighted in the screenshot below and download NekoRay. It doesn't need installation, just extract it somewhere in your computer (it doesn't matter where but preferably somewhere easy to find).

{{< button href="https://github.com/MatsuriDayo/nekoray/releases" >}}**NekoRay's GitHub Page**{{< /button >}}

![Nekoray-01](/images/nekoray-12.png)

2. Go to the folder where you extracted NekoRay and launch “nekoray” **as administrator**.

![Nekoray-02](/images/nekoray-13.png)

3. Click on the button that says “sing-box”

![Nekoray-03](/images/nekoray-1.png)

4. You will see the interface of the program in front of you. Click on the “Program” button at the top left corner.

![Nekoray-04](/images/nekoray-2.png)

5. Click on “Remember last profile”.

![Nekoray-05](/images/nekoray-3.png)

6. Copy the VPN URL of your of the protocol of your choice (VMess, VLess and/or Trojan) from below and then click on the “Program” button. This time, click on “Add profile from clipboard”.

{{< hint info >}}
vless://53b06cd2-1cbe-412c-9fcf-0904a9e0d214@vio0:4437?security=reality&sni=behindthename.com&fp=chrome&pbk=Ry9d1ODdg-muxLXP6vbW_Fh3_v5Ko95n6VYxQ9Rzny8&flow=xtls-rprx-vision#vless_testuser

vmess://c9d7b6c0-f076-4491-bdad-9d6910793b6e@vio0:4437?security=reality&sni=behindthename.com&fp=chrome&pbk=Ry9d1ODdg-muxLXP6vbW_Fh3_v5Ko95n6VYxQ9Rzny8&flow=xtls-rprx-vision#vmess_testuser

trojan://398b0152949db9245b795ae73444f7dd6d6aa84535d07b3fd04f0b769e64c915@vio0:4437?security=reality&sni=behindthename.com&fp=chrome&pbk=Ry9d1ODdg-muxLXP6vbW_Fh3_v5Ko95n6VYxQ9Rzny8#trojan_testuser
{{< /hint >}}

![Nekoray-06](/images/nekoray-4.png)

7. You will see that the VPN profile will appear in the middle. Right click on the VPN profile and choose “Start” (or click on the VPN profile and press Enter)

![Nekoray-07](/images/nekoray-6.png)

8. You will see a checkmark appear next to the VPN profile and the text turns blue. This happens when a VPN profile is selected. To select another profile, repeat the previous step (Step 5) on another profile.

9. In order to turn on the VPN and access the internet, you will need to click on either of the two VPN modes: “System Proxy” and “Tun Mode”. Click on “Tun Mode”. This will tunnel all of your computer's internet traffic through the VPN, this includes all the programs. (You need to run the program as Administrator in order to use “Tun Mode”. If you haven't done so, you will be asked whether or not you want to run the program as Administrator.).

![Nekoray-08](/images/nekoray-7.png)

10. After clicking on “Tun Mode”, you will notice that a red dot appears on the system tray icon of NekoRay. This is to indicate that “Tun Mode” is on.

![Nekoray-09](/images/nekoray-11.png)

11. To turn the VPN off, simply click on the “Tun Mode” checkbox again. Do remember to turn off the VPN when you're done using it. Do not turn your PC off or close the program while the VPN is connected.

12. And that's it! You can check your IP location to ensure that you are connected to the VPN and it's working properly.

## Other notes

1. You can turn the VPN on or off via the system tray icon. Right click on the system tray icon and go to system proxy and then choose either mode.

![Nekoray-10](/images/nekoray-8.png)

2. “System Proxy” mode activates the VPN via a proxy. This mode only works for browsers or web-clients (such as Discord's desktop app) and it will not work on any software is not browser-based (such as online games).

3. In case you forget to turn the VPN off before turning off your PC or closing the program, you might run into some connection issues. This can be solved by launching NekoRay and turning off the VPN mode that you previously selected.

4. In case you decide to change the program's settings and the client stops working, delete NekoRay's folder and download it again, and repeat the steps at the beginning of this tutorial.

5. If you wish to test the latency of the VPN profile, right click on the profile you want, go to “Current Select” and click on “Url Test”. The number that appears under “Test results” column is the latency. Alternatively, you can click on the bottom left of the program where the name of the selected profile is displayed and it will also tell you what the latency is.
