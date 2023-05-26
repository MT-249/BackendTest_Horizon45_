from django import forms

class driverForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.CharField(max_length=100, unique=True)
    username = forms.CharField(widget=forms.Textarea, unique=True)