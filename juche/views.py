from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'juche/home.html')


def historia(request):
    return render(request, 'juche/historia.html')


def zuche(request):
    return render(request, 'juche/zuche.html')


def songun(request):
    return render(request, 'juche/songun.html')


def byungjin(request):
    return render(request, 'juche/byungjin.html')


def mais(request):
    return render(request, 'juche/mais.html')
