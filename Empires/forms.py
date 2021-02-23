from django import forms
from Empires.models import AgeofEmpries



class AddEmpiresForm(forms.ModelForm):
  class Meta:
    model = AgeofEmpries
    fields = ['age']