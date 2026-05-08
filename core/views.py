from django.shortcuts import render, redirect
from .forms import ContatoForm, CadastroForm
from .models import Cliente, Cadastro


def home(request):

    if request.method == 'POST':
        form = ContatoForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('home')

    else:
        form = ContatoForm()

    clientes = Cliente.objects.all()

    return render(request, 'home.html', {
        'form': form,
        'clientes': clientes
    })

def cadastro(request):

    if request.method == 'POST':
        form = CadastroForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('cadastro')

    else:
        form = CadastroForm()

    return render(request, 'cadastro.html', {
        'form': form
    })