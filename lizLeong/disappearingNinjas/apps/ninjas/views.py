from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'ninjas/index.html')

def ninjas(request):
    return render(request, 'ninjas/ninjas.html')

def ninja_colors(request, color):
    colors = {
        "img" : 'ninjas/imgs/{}.png'.format(color),
    }
    if color not in ["blue", "red", "purple", "orange"]:
        colors['img'] = 'ninjas/imgs/kakashi.png'
    return render(request, 'ninjas/ninja_colors.html', colors)
