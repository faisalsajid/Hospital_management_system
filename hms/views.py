from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import *


@api_view(['GET', 'POST'])
def patientinfo(request):
    if request.method == 'POST':
        serializer = PatientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 200, 'message': 'Patient information saved successfully!'})
        return Response({'status': 400, 'errors': serializer.errors}, status=400)
    return render(request, 'patient_info.html')

@api_view(['GET'])
def patientdetails(request):
    patients = Patient.objects.all()
    serializer = PatientSerializer(patients, many=True)
    return Response(serializer.data)

def patientdetails_page(request):
    patients = Patient.objects.all().order_by('-id')
    return render(request, 'patient_details.html', {'patients': patients})


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('patientdetails_page')
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    return render(request, 'login.html')
