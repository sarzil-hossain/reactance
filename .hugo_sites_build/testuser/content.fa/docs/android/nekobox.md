---
title: NekoBox (V2Ray)
type: docs
weight: 1
---

# نِکوباکس (NekoBox)

در این آموزش یاد خواهید گرفت که چگونه از اپلیکیشن نِکوباکس روی دستگاه‌های اندرویدی استفاده کنید.

اپلیکیشن نِکوباکس از پروتکل‌های زیادی پشتیبانی می‌کند، و از این اپلیکیشن برای اتصال به پروتکل‌های اصلی‌مان روی دستگاه‌های اندرویدی استفاده خواهیم کرد. پروتکل‌هایی که مورد استفاده قرار خواهند گرفت عبارتند از: VLess، VMess و Trojan.

## نحوه نصب و استفاده از نِکوباکس:

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

۱۰. لینک پروتکل مورد نظرتان را از قسمت پایین کپی کنید.

{{< hint info >}}
vless://53b06cd2-1cbe-412c-9fcf-0904a9e0d214@vio0:4437?security=reality&sni=behindthename.com&fp=chrome&pbk=Ry9d1ODdg-muxLXP6vbW_Fh3_v5Ko95n6VYxQ9Rzny8&flow=xtls-rprx-vision#vless_testuser

vmess://c9d7b6c0-f076-4491-bdad-9d6910793b6e@vio0:4437?security=reality&sni=behindthename.com&fp=chrome&pbk=Ry9d1ODdg-muxLXP6vbW_Fh3_v5Ko95n6VYxQ9Rzny8&flow=xtls-rprx-vision#vmess_testuser

trojan://398b0152949db9245b795ae73444f7dd6d6aa84535d07b3fd04f0b769e64c915@vio0:4437?security=reality&sni=behindthename.com&fp=chrome&pbk=Ry9d1ODdg-muxLXP6vbW_Fh3_v5Ko95n6VYxQ9Rzny8#trojan_testuser
{{< /hint >}}

۱۱. در اپلیکیشن، روی علامت مثبت در بالای صحفه بزنید و **Import from Clipboard** را انتخاب کنید. (**نکته: ** اگر که لینک با موفقیت وارد برنامه شد ولی در صفحه اصلی برنامه چیزی ظاهر نشد، برنامه را ببندید و دوباره باز کنید تا در لیست ظاهر شود.)

![Nekobox-08](/images/nekobox-07.png)
![Nekobox-09](/images/nekobox-08.png)

۱۲. روی VPN که به تازگی ایجاد شد بزنید تا انتخاب شود. اگر چندین پروفایل در لیست دارید، آن که در کنارش نوار رنگی است انتخاب شده است.

۱۳. روی **دکمه** پایین صفحه بزنید تا به VPN وصل شوید.

![Nekobox-10](/images/nekobox-09.png)

۱۴. برای بررسی سرعت و تاخیر، در پایین صفحه روی نوشته **Connected, Tap to check connection** بزنید تا میزان تاخیر به میلی ثانیه به شما نشان داده شود.

![Nekobox-11](/images/nekobox-10.png)

۱۵. تمام! حال به VPN وصل شده‌اید. می‌توانید با استفاده از سایت‌های بررسی IP، لوکیشن خود را بررسی و از اتصال به VPN اطمینان حاصل کنید.
