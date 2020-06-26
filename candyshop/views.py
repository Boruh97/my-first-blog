from django.shortcuts import render, HttpResponse
from .models import BasePage
from pacet.models import Cake



def index(request):
    base_items = BasePage.objects.all()
    date = {
        'base':base_items
    }
    return render(request, 'index.html', context=date)


def cat(request):
    return render(request, 'cat.html')


def cake(request):
    cakes = Cake.objects.all()
    date = {
        'cakes': cakes
    }
    return render(request, 'cake.html', context=date)


def de_scripts(request):
    if request.method == 'POST':
        model_id = request.POST["id"]
        op = Cake.objects.get(id=model_id)
        date = {
            'info':op
        }

        return render(request, 'descript.html', context=date)

def base_de_scripts(request):
    if request.method == 'POST':
        model_id = request.POST["id"]
        op = BasePage.objects.get(id=model_id)
        date = {
            'info':op
        }

        return render(request, 'descript.html', context=date)