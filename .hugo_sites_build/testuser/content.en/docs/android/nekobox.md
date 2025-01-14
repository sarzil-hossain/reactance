---
title: NekoBox (V2Ray)
type: docs
weight: 1
---

# NekoBox

In this tutorial you will learn how to use NekoBox VPN client on android devices.

NekoBox is a VPN client supporting a variety of VPN protocols, and we will be using this handy client to use our main VPN protocols on android devices, including VLess, VMess, and Trojan.

## How to install and use NekoBox:

1. Go to NekoBox's GitHub page by clicking the button below. Download the APK that is compatible with your device. (In most cases, arm64-v8a version is compatible unless you have an old smartphone.)

{{< button href="https://github.com/MatsuriDayo/NekoBoxForAndroid/releases/tag/1.2.9" >}}**NekoBox's GitHub Page**{{< /button >}}

![Nekobox-01](/images/nekobox-12.png)

{{< hint danger >}}
**Warning**
The version of Nekobox that you can download from Google Play Store is not developed by the official developer of NekoBox, **please do not use that application.**
{{< /hint >}}

2. Install the application and open it.

3. Grant it the permission to send you notifications (if asked).

![Nekobox-02](/images/nekobox-01.png)

4. In the **“VpnService Policy”**, click on YES.

![Nekobox-03](/images/nekobox-02.png)

5. Download the NekoBox Settings file by clicking on the button below.

{{< button href="/nekoboxsetting/Nekobox-Settings.json" >}}**Download NekoBox Settings**{{< /button >}}

6. Open the **dashboard** by clicking on the menu icon on the top left corner of the interface and **“Tools”**.

![Nekobox-04](/images/nekobox-03.png)

7. Go to the **“Backup”** tab and click on **“Import from file”** button.

![Nekobox-05](/images/nekobox-04.png)

8. Select the setting file that you downloaded from **step 5**, then click on **“IMPORT”**.

![Nekobox-06](/images/nekobox-05.png)
![Nekobox-07](/images/nekobox-06.png)

9. If done **properly**, the UI should then turn **blue** and you should be brought back to the main screen of the app.

10. Copy the VPN URL of your of the protocol of your choice (**VMess**, **VLess** and/or **Trojan**) from below:

{{< hint info >}}
vless://53b06cd2-1cbe-412c-9fcf-0904a9e0d214@vio0:4437?security=reality&sni=behindthename.com&fp=chrome&pbk=Ry9d1ODdg-muxLXP6vbW_Fh3_v5Ko95n6VYxQ9Rzny8&flow=xtls-rprx-vision#vless_testuser

vmess://c9d7b6c0-f076-4491-bdad-9d6910793b6e@vio0:4437?security=reality&sni=behindthename.com&fp=chrome&pbk=Ry9d1ODdg-muxLXP6vbW_Fh3_v5Ko95n6VYxQ9Rzny8&flow=xtls-rprx-vision#vmess_testuser

trojan://398b0152949db9245b795ae73444f7dd6d6aa84535d07b3fd04f0b769e64c915@vio0:4437?security=reality&sni=behindthename.com&fp=chrome&pbk=Ry9d1ODdg-muxLXP6vbW_Fh3_v5Ko95n6VYxQ9Rzny8#trojan_testuser
{{< /hint >}}

11. In the app, click on the + icon on at the top of the interface, and select **“Import from Clipboard”**. (Note: If it's imported successfully but the VPN profle doesn't appear in the list of your VPN profiles, close the app and open it again, and it will appear in the list.)

![Nekobox-08](/images/nekobox-07.png)
![Nekobox-09](/images/nekobox-08.png)

12. Click on the VPN profile that was just added to select it. If you have multiple VPN profiles, the one that has a **highlight** on its left side is the one that is selected.

13. Click on the **button** at the bottom of the screen to connect to the VPN profile.

![Nekobox-10](/images/nekobox-09.png)

14. To check the latency of the VPN profile, click on the tab that says **“Connected, tap to check connection”**. It will tell you the latency in milliseconds.

![Nekobox-11](/images/nekobox-10.png)

15. And that's it! You can check your IP location to ensure that you are connected to the VPN and it's working properly.
