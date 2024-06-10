from django.urls import path
from . import views
app_name = "appointment"

urlpatterns = [
    path('',views.appointment_view,name="appointment"),
    path('appointment_for_eegSignal/',views.appointment_for_eegSignal,name="eeg-signal")
]
