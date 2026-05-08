from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContatoForm

def home(request):
    form = ContatoForm()

    return render(request, 'home.html', {
        'form': form
    })

# Create your views here.   
