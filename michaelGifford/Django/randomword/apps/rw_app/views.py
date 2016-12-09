from django.shortcuts import render, HttpResponse, redirect
import random as randm
import string


# Create your views here.
def id_generator(size=14, chars=string.ascii_uppercase + string.digits):
  return ''.join(randm.choice(chars) for _ in range(size))

def index(request):
    if 'count' not in request.session:
        request.session['count'] = 0
    if 'random' not in request.session:
        request.session['random'] = id_generator()
    return render(request, "rw_app/index.html")

def random(request):
    request.session['count'] += 1
    request.session['random'] = id_generator()
    return redirect('/')
