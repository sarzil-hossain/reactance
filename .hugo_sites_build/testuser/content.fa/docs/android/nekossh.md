---
title: SecureShell (SSH)
type: docs
weight: 1
---

# پروتکل SecureShell (SSH)

در این آموزش یاد خواهید گرفت که چگونه از نِکوباکس برای به کارگیری پروتکل SSH استفاده کنید.

اپلیکیشن نِکوباکس از پروتکل‌های زیادی پشتیبانی می‌کند، و  از این اپلیکیشن برای اتصال به پروتکل SSH استفاده خواهیم کرد.

**توجه داشته باشید که این پروتکل تنها در صورتی ارائه می‌شود که سایر پروتکل و متودها برای شما قابل استفاده نباشد.**

## نحوه نصب و استفاده از نِکوباکس برای استفاده از پروتکل SSH:

۱. روی دکمه زیر کلیک کنید تا به صفحه گیت‌هاب نِکوباکس بروید. فایل APK که با گوشی شما سازگار است را دانلود کنید. (در اکثر موارد، نسخه **arm64-v8a** با گوشی‌تان سازگار است، مگر این که دستگاه شما قدیمی باشد که در آن صورت نسخه **armeabi-v7a** را نصب کنید.)

{{< button href="https://github.com/MatsuriDayo/NekoBoxForAndroid/releases/tag/1.2.9" >}}**صفحه گیت‌هاب نِکوباکس**{{< /button >}}

![Nekobox-01](/images/nekobox-12.png)

{{< hint danger >}}
**اخطار**
اپلیکیشن نِکوباکس که در گوگل پلی استور است توسط خود سازنده‌های اصلی نِکوباکس ارائه نشده است. **از استفاده از آن نسخه خودداری کنید.**
{{< /hint >}}

۲. اپلیکیشن را نصب و اجرا کنید.

۳. در صورت لزوم، دسترسی‌های مورد نیاز را به اپلیکیشن بدهید (دسترسی به **اعلان‌ها**)

![Nekobox-02](/images/nekobox-01.png)

۴. در پیام بعدی، روی **YES** کلیک کنید.

![Nekobox-03](/images/nekobox-02.png)

۵. روی دکمه زیر کلیک کنید و فایل تنظیمات نِکوباکس را دانلود کنید.

{{< button href="/nekoboxsetting/Nekobox-Settings.json" >}}**دانلود تنظیمات نِکوباکس**{{< /button >}}

۶. در بالا سمت چپ، روی دکمه سه خط بزنید تا پنل **تنظیمات** باز شود. سپس، روی **Tools** بزنید.

![Nekobox-04](/images/nekobox-03.png)

۷. به قسمت **Backup** بروید و گزینه **Import from file** را انتخاب کنید.

![Nekobox-05](/images/nekobox-04.png)

۸. فایلی که در قدم **شماره 5** دانلود کردید را انتخاب کنید و سپس روی **IMPORT** بزنید.

![Nekobox-06](/images/nekobox-05.png)
![Nekobox-07](/images/nekobox-06.png)

۹. اگر قدم قبلی را **درست** انجام داده باشید، رنگ محیط کاربری به **آبی** تغییر می‌کند و به صفحه اصلی اپلیکیشن برمی‌گردید.

۱۰. در صفحه اصلی، روی گزینه مثبت در بالای صفحه بزنید و سپس **Manual** را انتخاب کنید. پس از آن، **SSH** را انتخاب کنید.

![NekoSSH-08](/images/nekobox-07.png)
![NekoSSH-09](/images/nekossh-01.png)
![NekoSSH-10](/images/nekossh-02.png)

۱۱. در صفحه‌ای که باز می‌شود، روی گزینه **Authentication Type** بزنید و آن را به **Public Key** تغییر دهید.

![NekoSSH-11](/images/nekossh-03.png)
![NekoSSH-12](/images/nekossh-04.png)

۱۲. حال موارد زیر را مطابق عکس در جاهای مربوطه کپی کنید.

۱. نام دلخواه خودتان

۲. 192.168.121.82

۳. **sshvpn**

۴. محتوای باکس زیر را به طور کامل کپی کنید و در قسمت **Private key** وارد کنید.

```bash
-----BEGIN OPENSSH PRIVATE KEY-----
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
loF+SSPYeledZQAAAAh0ZXN0dXNlcgE=
-----END OPENSSH PRIVATE KEY-----

```

![NekoSSH-13](/images/nekossh-05.png)

۱۳. پس از وارد کردن موارد قبلی، روی گزینه تیک در بالا سمت چپ بزنید. (نکته، اگر که لینک با موفقیت وارد برنامه شد ولی در صفحه اصلی برنامه چیزی ظاهر نشد، برنامه را ببندید و دوباره باز کنید تا در لیست ظاهر شود.)

۱۴. روی VPN که به تازگی ایجاد شد بزنید تا انتخاب شود. اگر چندین پروفایل در لیست دارید، آن که در کنارش نوار رنگی است انتخاب شده است.

۱۵. روی **دکمه** پایین صفحه بزنید تا به VPN وصل شوید.

![NekoSSH-14](/images/nekossh-06.png)

۱۶. برای بررسی سرعت و تاخیر، در پایین صفحه روی نوشته **Connected, Tap to check connection** بزنید تا میزان تاخیر به میلی ثانیه به شما نشان داده شود.

![NekoSSH-15](/images/nekobox-10.png)

۱۷. تمام! حال به VPN وصل شده‌اید. می‌توانید با استفاده از سایت‌های بررسی IP، لوکیشن خود را بررسی و از اتصال به VPN اطمینان حاصل کنید.
