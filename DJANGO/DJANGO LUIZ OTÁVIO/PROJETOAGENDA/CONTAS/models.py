from django.db import models
from CONTATOS.models import Contato
from django import forms

class FormContato(forms.ModelForm):
    class Meta:
        model = Contato
        exclude = ()