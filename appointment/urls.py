from django.urls import path
from .views import appointment_view
app_name = "appointment"

urlpatterns = [
    
    path('',appointment_view,name="appointment"),
]
