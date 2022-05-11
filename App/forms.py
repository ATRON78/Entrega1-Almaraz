from django import forms

class PadreForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    edad = forms.IntegerField()

class MadreForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    edad = forms.IntegerField()

class HermanoForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    edad = forms.IntegerField()