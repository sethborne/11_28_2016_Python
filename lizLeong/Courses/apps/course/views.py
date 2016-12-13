from django.shortcuts import render, redirect
from .models import Course

# Create your views here.
def index(request):
    context ={
        "courses":Course.objects.all(),
    }
    return render(request, 'course/index.html', context)

def add(request):
    Course.objects.create(name = request.POST['name'], description = request.POST['description'])
    return redirect('/')

def remove(request, id):
    Course.objects.filter(id=id).delete()
    return redirect('/')

#     SomeModel.objects.filter(id=id).delete()

# To delete it from an instance:
# instance = SomeModel.objects.get(id=id)
# instance.delete()

def check(request, id):
    context={
        'course_info':Course.objects.get(id=id)
    }
    return render(request, 'course/remove.html', context)

# def index(request):
#     return
