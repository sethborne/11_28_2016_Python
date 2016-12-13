from django.shortcuts import render, HttpResponse
import time

def index(request):
    context = {
        'key1': "WOW",
        'key2': "Bunana peel",
        'time': time.strftime("%A %X %x"),
    }
    return render(request, 'timedisplay/index.html', context)



# Create your views here.
