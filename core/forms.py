from django import forms
from .models import Cliente, Cadastro


class ContatoForm(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = ['nome', 'email']


class CadastroForm(forms.ModelForm):

    class Meta:
        model = Cadastro
        fields = "__all__"