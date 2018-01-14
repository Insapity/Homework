from django import forms
from my_app.models import *


class RegistrForm(forms.ModelForm):
    class Meta:
        model = Registr
        fields = ["id_registr", "code_registr", "nomer_registr"]
        #widgets = {'information': forms.Textarea(attrs={'resize': 'none'})}


class HumanForm(forms.ModelForm):
    class Meta:
        model = Human
        fields = ["id_human", "fio", "registr_code"]
        #widgets = {'information': forms.Textarea(attrs={'resize': 'none'})}
