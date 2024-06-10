from django.shortcuts import render
from .models import AppointmentModel
# Create your views here.

def appointment_view(request):
    return render(request,'appointment/index.html')


#url for show appointment 
def appointment_for_eegSignal(request):
    all_appointment_eeg_signal = AppointmentModel.objects.all()
    context = {"datas":all_appointment_eeg_signal}
    return render(request,"appointment/appointment_eeg_signal.html",context)
