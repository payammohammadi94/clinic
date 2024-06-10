from django.db import models
from jalali_date import datetime2jalali
from django.contrib.auth.models import User
'''
این مدل برای دریافت نوبت برای سیگنال مغری می‌باشد
'''
# Create your models here.

#model for days
'''
شنبه
یکشنبه
دوشنبه
...
'''
class weeksTimeModel(models.Model):
    class Meta:
        verbose_name = "روز های هفته "
        verbose_name_plural = "روز های هفته"
            
    weeks_time = models.CharField(max_length=10,verbose_name="روزهای هفته")
    def __str__(self):
        return self.weeks_time
    
    
#model for time visit for example (3 - 3:30)-(3:30 - 4)-...
'''
ساعت های نوبت دهی را در اینجا وارد میکنیم که بعدا بتوانیم استفاده کنیم.
'''
class TimesVisitModel(models.Model):
    class Meta:
        verbose_name = "ساعت های ویزیت"
        verbose_name_plural = "ساعت های ویزیت"    
    
    time = models.CharField(max_length=30,verbose_name="ساعت نوبت دادن")
    def __str__(self):
        return self.time
    
class AppointmentModel(models.Model):
    class Meta:
        verbose_name = "نوبت دهی سیگنال‌های مغزی EEG"
        verbose_name_plural ="نوبت دهی سیگنال‌های مغزی EEG"
    
    
    
    DAYS_CHOICES = (
                    (1, 1),
                    (2, 2),
                    (3, 3),
                    (4, 4),
                    (5, 5),
                    (6, 6),
                    (7, 7),
                    (8, 8),
                    (9, 9),
                    (10, 10),
                    (11, 11),
                    (12, 12),
                    (13, 13),
                    (14, 14),
                    (15, 15),
                    (16, 16),
                    (17, 17),
                    (18, 18),
                    (19, 19),
                    (20, 20),
                    (21, 21),
                    (22, 22),
                    (23, 23),
                    (24, 24),
                    (25, 25),
                    (26, 26),
                    (27, 27),
                    (28, 28),
                    (29, 29),
                    (30, 30),
                    (31, 31))
    
    MONTHS_CHOICES = ((1,"فروردین"),
                      (2,"اردیبهشت"),
                      (3,"خرداد"),
                      (4,"تیر"),
                      (5,"مرداد"),
                      (6,"شهریور"),
                      (7,"مهر"),
                      (8,"آبان"),
                      (9,"آذر"),
                      (10,"دی"),
                      (11,"بهمن"),
                      (12,"اسفند"),)
    
    YEARS_CHOICES = ((1403,1403),(1404,1404),(1405,1405),(1406,1406),(1407,1407),)
    
    weeks_day = models.ForeignKey(weeksTimeModel,on_delete=models.CASCADE,verbose_name="روز هفته")
    
    day = models.IntegerField(choices=DAYS_CHOICES,verbose_name="تاریخ-روز")
    month = models.IntegerField(choices=MONTHS_CHOICES,verbose_name="تاریخ-ماه")
    year = models.IntegerField(choices = YEARS_CHOICES,verbose_name="تاریخ سال")
    
    
    time = models.ManyToManyField(TimesVisitModel,related_name='times',verbose_name="زمان های ویزیت")
    
    create = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return str(self.weeks_day) + "- (" + str(self.day) +"-"+str(self.month)+"-"+str(self.year) + ")"

    def count_time(self):
        return self.time.count()
    
    

class GetAppointmentModel(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    code_meli = models.CharField(max_length=12)
    phone = models.CharField(max_length=12)
    
   
    # هر شخصی نوبت گرفت یه کدی به آن اختصاص می‌دهیم تا بعدا به راحتی درون دیتا بیس پیدا کنیم.
    code_nobat = models.BigIntegerField()
    #time for visit
    #وقتی کاربر روی یک تایم کلیک کرد ما آن رد درون این مدل ذخیره میکنیم و درون لیست نوبت ها هم حذف می‌کنیم.
    time_visit = models.CharField(max_length=50)
    create = models.DateTimeField(auto_now=True)
    update = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.phone + self.first_name
    