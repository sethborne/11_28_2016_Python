from django.shortcuts import render, redirect
from django.contrib import messages
import re
from .models import Email
# Create your views here.



def index(request):

    return render(request, 'emailcheck/index.html')

def validate(request):
    email = request.POST['email']
    print email
    email_regex = re.match(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$', email)

    if email_regex != None:
        print "it worked"
        request.session['email'] = request.POST['email']
        Email.objects.create(email=request.POST['email'])
        context = {
            "emails" : Email.objects.all(),
        }
        return render(request, 'emailcheck/success.html', context)
    else:
        messages.warning(request, "Your e-mail address isn't valid. Please fix it.")
        return redirect('/')

def delete(request, id):
    context = {
        "emails" : Email.objects.all(),
    }
    Email.objects.get(id=id).delete()
    deleted = "yes"
    print deleted
    return redirect('/')

def users(request):
    context = {
        "emails" : Email.objects.all(),
    }
    try:
        del request.session['email']
    except:
        KeyError
    return render(request, 'emailcheck/success.html', context)
