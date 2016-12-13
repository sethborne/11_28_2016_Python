from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages

# Create your views here.
def index(request):
    if not 'count' in request.session:
        request.session['count'] = 0
    return render(request, 'form/index.html')

def process(request):
    name = request.POST['name']
    comment = request.POST['comments']
    if len(name) > 0 and len(comment) > 0:
        request.session['name'] = name
        request.session['location'] = request.POST['location']
        request.session['language'] = request.POST['language']
        request.session['comment'] = comment
        request.session['count'] += 1
    else:
        messages.add_message(request, messages.INFO, "Please fill all fields!")
        return redirect('/')
    return redirect('/results')

def results(request):
    return render(request, 'form/results.html')
