from django.shortcuts import render, redirect
from .models import Course, Description

# Create your views here.
def index(request):
    context = {
        'all_courses': Course.objects.all(),
    }
    return render(request, 'main/index.html', context)

def add_course(request):
    description = Description.objects.create(content = request.POST['description'])
    print description
    Course.objects.create(name = request.POST['name'], description = description)
    return redirect('/')

def destroy(request, course_id):
    context = {
        'course': Course.objects.get(id=course_id),
    }
    return render(request, 'main/show.html', context)

def delete(request, course_id):
    Course.objects.get(id = course_id).delete()
    return redirect('/')
