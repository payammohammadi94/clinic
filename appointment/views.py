from django.shortcuts import render

# Create your views here.

def appointment_view(request):
    return render(request,'appointment/index.html')
