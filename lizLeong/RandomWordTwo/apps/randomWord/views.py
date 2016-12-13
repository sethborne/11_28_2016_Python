from django.shortcuts import render, HttpResponse, redirect
import string
import random


# Create your views here.
def index(request):
    if not 'attempt' in request.session:
        request.session['attempt'] = 0
        request.session['randomWord'] = 'Click Button to Generate a Random String'
    return render(request, 'randomWord/index.html')

def newWord(request):
    request.session['attempt'] += 1
    request.session['randomWord'] = ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(14)])
    print "*" * 100
    return redirect('/')

def reset(request):
    request.session.clear()
    return redirect('/')
