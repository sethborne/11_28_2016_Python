from django.shortcuts import render, HttpResponse

# def index(request):
#     response ="Hello, I am your frist request!"
#     return HttpResponse(response)

def index(request):
    print("*" * 100)
    return render(request, "first_app/index.html")

# Create your views here.
# CONTROLLER
