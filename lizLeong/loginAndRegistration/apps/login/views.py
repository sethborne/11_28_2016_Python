from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import User

# Create your views here.
def index(request):
    return render(request, 'login/index.html')

def register(request):
     response = User.objects.validate(request.POST)
     if not response['status']:
            for error in response['errors']:
                messages.error(request, error)
            return redirect ('/')
     else:
         user = User.objects.get(email = request.POST['email'])
         request.session['id'] = user.id
         print request.session['id']
     return redirect('/success')
     #EVERYTHING BREAKS, MAKE SURE THE QUERIES USE A UNIWUE THINg

    #     response = Author.objects.add_author(request.POST)
    # if not response['status']:
    #     for error in response['errors']:
    #         messages.error(request, error)
    # # Author.objects.create(name = request.POST['name'])
    # return redirect('/')

def login(request):
    response = User.objects.login(request.POST)
    if not response['status']:
        for error in response['errors']:
            messages.error(request,error)
        return redirect('/')
    else:
        user = User.objects.get(email = request.POST['email'])
        request.session['id'] = user.id
        return redirect('/success')

def logout(request):
    request.session.clear()
    return redirect ('/')

def success(request):
    if request.session['id']:
        context ={
            'users': User.objects.get(id = request.session['id'])
        }
    return render(request, 'login/success.html', context)
