from django import forms
from django.db.models import fields
from django.contrib.auth.forms import ReadOnlyPasswordHashField, UserCreationForm,UserChangeForm
from django.db.models.query_utils import FilteredRelation
from django.shortcuts import get_object_or_404
from . import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from .models import Profile
from phone_field import PhoneFormField
## make your forms registrations


class userform(UserCreationForm):
    username = forms.CharField(widget= forms.TextInput
                           (attrs={'placeholder':'Enter your username','class':'text-input'}))
    email = forms.CharField(widget= forms.EmailInput
                           (attrs={'placeholder':'Enter your Email','class':'text-input'}))
    password1 = forms.CharField(widget=forms.PasswordInput (attrs={'placeholder':'Enter password','class':'text-input'}))
    password2 = forms.CharField(widget=forms.PasswordInput (attrs={'placeholder':'confirm password','class':'text-input'}))

    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class profileform(forms.ModelForm):
    address=forms.CharField(widget=forms.TextInput (attrs={'class':'text-input w-100','placeholder':'address 13 appar name ... '}))
    fullname=forms.CharField(widget=forms.TextInput (attrs={'class':'text-input','placeholder':' enter your name .. '}))
    country=CountryField()
    ZipCode=forms.CharField(widget=forms.TextInput (attrs={'class':'text-input w-25','placeholder':'ZipCode'}))
    city = forms.CharField(widget=forms.TextInput (attrs={'class':'text-input w-75','placeholder':'enter your city'}))
    phone= PhoneFormField()
    class Meta:
        model = models.Profile
        fields = ['address','country','fullname','ZipCode','city','phone']

class userchange(UserChangeForm):
    email = forms.CharField(widget= forms.EmailInput
                           (attrs={'class':'text-input'})) 
    username = forms.CharField(widget= forms.TextInput
                           (attrs={'class':'text-input'}))
    class Meta:
        model = User
        fields = ['username','password','email']

class Emailsform(forms.ModelForm):
    Email_text = forms.EmailField(widget= forms.EmailInput
                           (attrs={'class':'text-input email'}),label='')
    class Meta:
        model = models.Email
        fields = ('Email_text',)