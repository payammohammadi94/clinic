from django.contrib import admin
from .models import weeksTimeModel, TimesVisitModel, AppointmentModel
# Register your models here.


class weeksTimeModelAdmin(admin.ModelAdmin):
    list_display = ("weeks_time",)
    search_fields = ("weeks_time",)
    
admin.site.register(weeksTimeModel,weeksTimeModelAdmin)
#########################

class TimesVisitModelAdmin(admin.ModelAdmin):
    list_display = ("time",)
    search_fields = ("time",)
    
    
admin.site.register(TimesVisitModel,TimesVisitModelAdmin)
######################################


class AppointmentModelAdmin(admin.ModelAdmin):
    list_display = (
        "weeks_day",
        "day",
        "month",
        "year",)
    search_fields = ("weeks_day",
                    "day",
                    "month",
                    "year",) 
    

    
admin.site.register(AppointmentModel,AppointmentModelAdmin)