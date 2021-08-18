from django.http.response import HttpResponse
from django.shortcuts import render
from .models import userdetails


# Create your views here.

def home(request):
    if request.method=='POST':
        if request.POST['type']=='doctortype':
           return render(request,"tss1/doctor.html")
        elif request.POST['type']=='patienttype':
            return render(request,"tss1/patient.html")   
             
    else:
        return render(request,"tss1/index.html") 

def doctor(request):
    if request.method=='POST':
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        email=request.POST['email']
        number=request.POST['number']
        type=request.POST['type']
        user=userdetails.objects.create(firstname=firstname,lastname=lastname,email=email,number=number,type=type)
        user.save()
        return HttpResponse("Congratulations! User created succesfully")