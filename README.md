# Pomodoro technique

In short, The Pomodoro Technique is a time management method based on 25-minute stretches of focused work broken by
five-minute breaks. Longer breaks, typically 15 to 30 minutes, are taken after four consecutive work intervals.
Each work interval is called a pomodoro, the Italian word for tomato.

The Pomodoro technique is designed to improve productivity and focus by breaking down tasks into manageable chunks
and avoiding distractions.

It can be run from the command line with various options to specify work durations or rest periods, or use the
default values of 25 minutes for work and 5 minutes for rest. The script accepts the following arguments:

 `  -t    set the work period in minutes `
 `  -b    set the break period in minutes `
 `  -h    display the help message`

It uses the "time" module to measure elapsed time and update the page every second with a countdown and progress.
The countdown shows the minutes and seconds remaining, while the progress bar shows how much of the current period
has been completed using the 🍅 and - symbols.


we also uses the `subprocess.Popen()` function from the `subprocess` module to send notification messages when the
time is up, depending on the operating system.
The notification messages can be customized by passing them as arguments to the `tomato()` function, which takes
two parameters: minutes and notification. `(supports three types of notifications.)`


The script can be interrupted at any time by pressing `Ctrl+C`,
 which will print a goodbye message and exit gracefully.


`One of the accessible examples of this program is in the Windows clock as an extension`


به طور خلاصه، تکنیک پومودورو یک روش مدیریت زمان است که بر اساس کارهای متمرکز 25 دقیقه ای شکسته شده است
استراحت های پنج دقیقه ای استراحت های طولانی تر، معمولاً 15 تا 30 دقیقه، پس از چهار فاصله کاری متوالی گرفته می شود
هر فاصله کاری پومودورو، کلمه ایتالیایی گوجه فرنگی نامیده می شود

تکنیک پومودورو برای بهبود بهره وری و تمرکز با تقسیم کردن وظایف به بخش های قابل مدیریت
و اجتناب از حواس پرتی طراحی شده است


می توان آن را از خط فرمان با گزینه های مختلف برای تعیین مدت زمان کار یا دوره های استراحت اجرا کرد
 یا از مقادیر پیش فرض 25 دقیقه برای کار و 5 دقیقه برای استراحت استفاده کرد.
  اسکریپت آرگومان های زیر را می پذیرد:

  ` -t دوره کار را بر حسب دقیقه تنظیم کنید`
  ` -b دوره استراحت را بر حسب دقیقه تنظیم کنید`
  ` -h پیام راهنما را نمایش می دهد`

از ماژول "زمان" برای اندازه گیری زمان سپری شده استفاده می کند
 و هر ثانیه صفحه را با شمارش معکوس و پیشرفت به روز می کند.

 شمارش معکوس دقیقه ها و ثانیه های باقیمانده را نشان می دهد،
  در حالی که نوار پیشرفت نشان می دهد که چه مقدار از دوره جاری است

  با استفاده از نمادهای 🍅 و - تکمیل شده است

ما همچنین از تابع "subprocess.Popen()" از ماژول "subprocess" برای ارسال پیام های اعلان استفاده می کنیم.
زمان بسته به سیستم عامل تمام شده است.

پیام‌های اعلان را می‌توان با ارسال آن‌ها به عنوان آرگومان به تابع «tomato()» سفارشی کرد.
دو پارامتر: دقیقه و اعلان. `(از سه نوع اعلان پشتیبانی می کند.)`



اسکریپت می تواند در هر زمان با فشار دادن "Ctrl+C" قطع شود،
  که پیام خداحافظی را چاپ می کند و به آرامی خارج می شود.

  ` یکی از نمونه های قابل دسترس این برنامه در ساعت ویندوز به عنوان اکستنشن قرار دارد`
