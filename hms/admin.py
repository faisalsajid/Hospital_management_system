from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name', 'age', 'phone_number', 'address']
    search_fields = ['full_name', 'phone_number']
    list_filter = ['age']


@admin.register(doctor)
class doctorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'userid', 'specialization', 'phone_number', 'address']
    search_fields = ['name', 'userid']
    list_filter = ['specialization']