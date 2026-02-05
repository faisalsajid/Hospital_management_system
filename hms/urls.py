from django.urls import path
from hms.views import *


urlpatterns = [
    path('patientdetails/', patientdetails, name='patientdetails'),
    path('patientinfo/', patientinfo, name='patientinfo'),
    path('login/', login, name='login'),
]