from django import forms
from django.forms import models
from .models import guestcostumer

class getemail(forms.ModelForm):
    email_costumer = forms.EmailField(widget=forms.TextInput ({'id':'input','name':'input','placeholder':'enter your Email...'}),required=True)
    class Meta:
        model= guestcostumer
        fields = ['email_costumer']

