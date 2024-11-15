---
title: SecureShell (SSH)
type: docs
weight: 1
---

# SecureShell (SSH) on NekoBox

In this tutorial you will learn how to make use of the SSH VPN service using NekoBox.

NekoBox is a VPN client supporting a variety of VPN protocols, and we will be using this handy client to use SecureShell (SSH) VPN protocol.

**Please note that SSH is meant to be used as a last resort option in case the other methods don't work.**

## How to install and use NekoBox for SSH VPN:

1. Go to NekoBox's GitHub page by clicking the link below. Download the APK that is compatible with your device. (In most cases, arm64-v8a version is compatible unless you have an old smartphone.)

{{< button href="https://github.com/MatsuriDayo/NekoBoxForAndroid/releases/tag/1.2.9" >}}**NekoBox's GitHub Page**{{< /button >}}

![NekoSSH-01](/images/nekobox-12.png)

{{< hint danger >}}
**Warning**
The version of Nekobox that you can download from Google Play Store is not developed by the official developer of NekoBox, **please do not use that application.**
{{< /hint >}}

2. Install the application and open it.

3. Grant it the permission to send you notifications (if asked).

![NekoSSH-02](/images/nekobox-01.png)

4. In the **“VpnService Policy”**, click on YES.

![NekoSSH-03](/images/nekobox-02.png)

5. Download the NekoBox Settings file by clicking on the link below.

[**Download NekoBox Settings**](/nekoboxsettings/Nekobox-Settings.json)

6. Open the **dashboard** by clicking on the menu icon on the top left corner of the interface and **“Tools”**.

![NekoSSH-04](/images/nekobox-03.png)

7. Go to the **“Backup”** tab and click on **“Import from file”** button.

![NekoSSH-05](/images/nekobox-04.png)

8. Select the setting file that you downloaded from **step 5**, then click on **“IMPORT”**.

![NekoSSH-06](/images/nekobox-05.png)
![NekoSSH-07](/images/nekobox-06.png)

9. If done **properly**, the UI should then turn **blue** and you should be brought back to the main screen of the app.

10. In the app, click on the + icon on at the top of the interface, and select **"Manual"**, then click on **"SSH"** 

![NekoSSH-08](/images/nekobox-07.png)
![NekoSSH-09](/images/nekossh-01.png)
![NekoSSH-10](/images/nekossh-02.png)

11. In the next menu, click on the option that says **"Authentication Type"** and change it to **"Public Key".**

![NekoSSH-11](/images/nekossh-03.png)
![NekoSSH-12](/images/nekossh-04.png)

12. Once you've done the preivous step, **copy** and **paste** the following values in their respective fields.

	1. Any name that you want.

	2. 192.168.121.82

	3. **sshvpn**

	4. Copy and paste the entire box below and paste it in field **#4**.

```bash
-----BEGIN OPENSSH PRIVATE KEY-----
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
loF+SSPYeledZQAAAAh0ZXN0dXNlcgE=
-----END OPENSSH PRIVATE KEY-----

```

![NekoSSH-13](/images/nekossh-05.png)

13. Once done, click on the checkmark button at top right corner. (Note: If it's imported successfully but the VPN profle doesn't appear in the list of your VPN profiles, close the app and open it again, and it will appear in the list.)

14. Click on the VPN profile that was just added to select it. If you have multiple VPN profiles, the one that has a **highlight** on its left side is the one that is selected.

13. Click on the **button** at the bottom of the screen to connect to the VPN profile.

![NekoSSH-14](/images/nekossh-06.png)

14. To check the latency of the VPN profile, click on the tab that says **“Connected, tap to check connection”**. It will tell you the latency in milliseconds.

![NekoSSH-15](/images/nekobox-10.png)

15. And that's it! You can check your IP location to ensure that you are connected to the VPN and it's working properly.
