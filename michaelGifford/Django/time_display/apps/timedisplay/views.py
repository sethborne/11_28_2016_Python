from django.shortcuts import render, HttpResponse
import datetime
from django.utils import timezone


# Create your views here.
def index(request):
    data = {
        'time': datetime.datetime.now()
    }
    return render(request, 'timedisplay/index.html', data)
