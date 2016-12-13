from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
import re

email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
name_regex = re.compile(r'^[A-Za-z]{2,}$')
password_regex = re.compile(r'^[a-zA-Z0-9]{8,}$')

# Create your views here.
def index(request):
    return render(request, 'loginreg/index.html')

def register(request):
    request.session['first_name'] = request.POST['first_name']
    request.session['last_name'] = request.POST['last_name']
    request.session['email'] = request.POST['email']
    response = User.userManager.regvalidate(request.POST)
    print response
    if not response['status'] == True:
        for error in response['errors']:
            messages.error(request, error)
        return redirect('/')


    context = {
        "users": User.userManager.all()
    }
    newUser = True
    return render(request, 'loginreg/success.html', context)

def login(request):
    request.session['loginemail'] = request.POST['loginemail']
    loginresponse = User.userManager.logvalidate(request, request.POST['loginemail'], request.POST['loginpassword'])
    print loginresponse
    context = {
        "users": User.userManager.all()
    }
    if not loginresponse['status'] == True:
        for error in loginresponse['errors']:
            messages.error(request, error)
            print error
            return redirect('/')
    if loginresponse['status'] == True:
        return render(request, 'loginreg/success.html', context)

def delete(request, id):
    context = {
        "users" : User.userManager.all(),
    }
    User.userManager.get(id=id).delete()
    return redirect('/')
