from django.shortcuts import render, redirect, HttpResponse
from .models import Email
import re
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'validation/index.html')

def validate(request):
    email = Email.objects.validate(request.POST['email'])
    #check what is in email
    print email
    #use email here because the dictionary returned from validate is stored in email variable
    #check for certain keys in email dictionary
    if 'email' in email:
        Email.objects.create(email = email['email']) #or email = request.POST['email']?
        return redirect ('/success')
    if 'error' in email:
        messages.add_message(request, messages.INFO, email['error']) #or just string 'Invalid email'??
        return redirect('/')

    # valid_email = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
    # if valid_email.match(request.POST['email']): ##add stoof here
    #     Email.objects.create(email = request.POST['email'])
    #     return redirect ('/success')
    # else:
    #     messages.add_message(request, messages.INFO, "Invalid email format, try again >:(") # add message here "invalid email"
    #     return redirect('/')

        # # Inside your app's views.py file
        #   from django.shortcuts import render, HttpResponse, redirect
        #   from .models import User
        #   def index(request):
        #       print("Running index method, calling out to User.")
        #       user = User.objects.login("speros@codingdojo.com","Speros")
        #
        # # DO NOT PASS THE WHOLE REQUEST OBJECT TO THE MODEL!!!
        #       print (type(user))
        #       if 'error' in user:
        #           pass
        #       if 'theuser' in user:
        #           pass
        #       return HttpResponse("Done running userManager method. Check your terminal console.")

# r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$'
#
# import re
# pattern = re.compile("^([A-Z][0-9]+)+$")
# pattern.match(string)

def success(request):
    context ={
        'emails': Email.objects.all(),
    }
    return render(request, 'validation/success.html', context)
