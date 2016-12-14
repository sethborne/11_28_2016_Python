from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'loginReg/index.html')

def register(request):
    viewsResponse = User.objects.add_user(request.POST)
    if viewsResponse['isRegistered']:
        request.session['user_id'] = viewsResponse['user'].id
        request.session['user_fname'] = viewsResponse['user'].first_name
        return redirect('users:success')
    else:
        for error in viewsResponse['errors']:
            messages.error(request, error)
        return redirect('users:index')

def success(request):
    if 'user_id' not in request.session:
        messages.error(request, 'Must be logged in!')
        return redirect('users:index')
    return render(request, 'loginReg/success.html')

def login(request):
    viewsResponse = User.objects.login_user(request.POST)
    if viewsResponse['isLoggedIn']:
        request.session['user_id'] = viewsResponse['user'].id
        request.session['user_fname'] = viewsResponse['user'].first_name
        return redirect('users:success')
    else:
        for error in viewsResponse['errors']:
            messages.error(request, error)
        return redirect('users:index')

def logout(request):
    request.session.clear()
    return redirect('users:index')
