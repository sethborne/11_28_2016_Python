from django.shortcuts import render, HttpResponse, redirect


def index(request):
    return render(request, "survey/index.html")

def post(request):
    data = {
        'name':request.POST['name'],
        'location':request.POST['location'],
        'language':request.POST['language'],
        'comment':request.POST['comment']
    }
    print (data)
    request.session['data'] = data
    if 'count' in request.session:
        request.session['count'] += 1
    else:
        request.session['count'] = 1
    return redirect('/result')

def result(request):
    return render(request, 'survey/results.html')
