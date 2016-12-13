from django.shortcuts import render, redirect
from .models import Course

# Create your views here.
def index(request):
    context = {
        "courses" : Course.objects.all()
    }
    return render(request, 'courselist/index.html', context)

def addcourse(request):
    Course.objects.create(title=request.POST['title'], description=request.POST['description'])
    return redirect('/')

def confirm(request, id):
    context = {
        "courses" : Course.objects.filter(id = id),
        "id" : id
    }
    return render(request, 'courselist/delete.html', context, id)

def destroy(request, id):
    Course.objects.get(id=id).delete()
    return redirect('/')
