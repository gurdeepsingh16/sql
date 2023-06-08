from django.shortcuts import render
from .models import *
from .form import User_register
from django.contrib import auth
from django.contrib.auth import login,logout
# Create your views here.

def User_register_function(request):
    if request.method == "GET":
        form = User_register()
        return render(request,"register.html",{'form':form})
    else:
        form = User_register(request.POST)
        if form.is_valid():
            form.save()

    return render(request,"register.html")


def login_function(request):
    if request.method=="POST":
        name = request.POST['name']
        password = request.POST['password']
        print(name,password)
        user = auth.authenticate(name=name,password=password)

        print(user)
        if user is not None:
            login(request,user)
        else:
            print("dfaa ho")

    return render(request,'login.html')

