---
title: OpenConnect
type: docs
---

# OpenConnect

## How to install and use OpenConnect client on Windows devices:

1. Go to the OpenConnect client's GitLab page by clicking the button below. Click on the link that is marked in the screenshot below. Installation is straightforward and very easy.

{{< button href="https://gitlab.com/openconnect/openconnect-gui/-/releases" >}}**OpenConnect client GitLab Page**{{< /button >}}

![Openconnect-01](/images/windows-oc-01.png)

2. It should prompt you to install a distributable and a network adapter, give it permission to do so.

3. Open the client, click on the gear icon in the middle, then click on **“New profile (Advanced)”**

![Openconnect-02](/images/windows-oc-02.png)

4. Download the two files that are provided below:

	1. **User Certificate:** [Click to download User Certificate](/testuser-User-Certificate.pem)

	2. **User Key:** [Click to download User Key](/testuser-User-Key.pem)

5. Do the following in the given order:

	1. Enter a **name** (any name you want)

	2. Copy the following and paste it in the server address field: **192.168.121.82:4430**

	3. Click on the button next to the **“User Certificated”** field, and choose the User Certificate file that you downloaded from **step 4**.

	4. Click on the button next to the **“User Key”** field, and choose the User Key  file that you downloaded from **step 4**.

![Openconnect-03](/images/windows-oc-03.png)
![Openconnect-04](/images/windows-oc-04.png)

6. Click save, then click on the big button in the middle saying **"connect"**.

![Openconnect-05](/images/windows-oc-05.png)

7. You'll be prompted to confirm the information regarding the destination address. Click on **“Accurate information”**.

![Openconnect-06](/images/windows-oc-06.png)

8. To disconnect the VPN, simply click on the **Disconnect** button in the main interface.

![Openconnect-07](/images/windows-oc-08.png)

9. And that's it! You can check your IP location to ensure that you are connected to the VPN and it's working properly.