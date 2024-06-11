from django.shortcuts import render
from .models import AppointmentModel
from django.shortcuts import get_object_or_404
# Create your views here.

def appointment_view(request):
    return render(request,'appointment/index.html')


#url for show appointment 
def appointment_for_eegSignal(request):
    all_appointment_eeg_signal = AppointmentModel.objects.all()
    
    print(len(all_appointment_eeg_signal))
    context = {"datas":all_appointment_eeg_signal}
    return render(request,"appointment/appointment_eeg_signal.html",context)



def choice_time_for_eegSignal(request,id):
    appointment_choices = get_object_or_404(AppointmentModel, pk=id)
    times_for_day = appointment_choices.time.all()
    context = {"data":appointment_choices,"times":times_for_day}
    return render(request,"appointment/choice_appointment_eeg_signal.html",context)
    
