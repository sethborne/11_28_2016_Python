from django.shortcuts import render, redirect
import random, datetime

# Create your views here.
def index(request):
    if 'totalGold' not in request.session:
        request.session['totalGold'] = 0
    return render(request, 'buildings/index.html')
def process_money(request):
    if 'activites' not in request.session:
        request.session['activites'] = []
    activity = {}
    buildings = {
        'farm': int(random.randint(10,20)),
        'cave': int(random.randint(5,10)),
        'house': int(random.randint(2,5)),
        'casino': int(random.randint(-50,50)),
    }
    if request.POST['building'] in buildings:
        request.session['totalGold'] += buildings[request.POST['building']]

    time = datetime.datetime.now().strftime('%h %d, %Y @ %I:%m:%S')

    if buildings[request.POST['building']] < 0:
        style = 'lost'
        result = 'Entered a casino and lost {} goals....Ouch! ({})'.format(abs(buildings[request.POST['building']]), time)
    else:
        style = 'gained'
        result = 'Earned {} from the cave! ({})'.format(buildings[request.POST['building']], time)

    activity['class'] = style
    activity['result'] = result
    request.session['activites'].append(activity)

    return redirect('/')

def reset(request):
    request.session.clear()
    return redirect('/')
