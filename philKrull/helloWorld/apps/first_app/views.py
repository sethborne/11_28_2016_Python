from django.shortcuts import render

# Create your views here.
# 12 create method based upon route from urls
def index(request):
# 13 render a page through the templates/apps folder
    return render(request, 'first_app/index.html')
