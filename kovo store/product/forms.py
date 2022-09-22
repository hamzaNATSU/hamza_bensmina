from django.db import models
from django.forms.widgets import Textarea
from settings.models import Variant
from crispy_forms.helper import FormHelper
from crispy_forms.bootstrap import StrictButton
from crispy_forms.layout import Field, Layout
from django import forms
from django.db.models import fields
from django.db.models.fields import CharField, EmailField, NullBooleanField
from django_filters.fields import RangeField
from .models import OrderItem, shippingAdress
from phone_field import PhoneFormField
from django_countries.fields import CountryField



class ProductFilterFormHelper(forms.Form):
    def __init__ (self, *args, **kwargs):
        super(). __init__ (*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'GET'
        layout_fields = []
        for field_name, field in self.fields.items():
            if isinstance(field, RangeField):
                layout_field = Field(field_name, template="forms/fields/range-slider.html")
            else:
                layout_field = Field(field_name)
            layout_fields.append(layout_field)
        layout_fields.append(StrictButton("Submit", name='submit', type='submit'))
        self.helper.layout = Layout(*layout_fields)



class orderAdressForm (forms.ModelForm):
    address = forms.CharField(widget=forms.TextInput (attrs={'class':'text-input w-100','placeholder':'Enter the delivery address '}))
    ZipCode=forms.CharField(widget=forms.TextInput (attrs={'class':'text-input w-50','placeholder':'ZipCode'}))
    city = forms.CharField(widget=forms.TextInput (attrs={'class':'text-input w-75','placeholder':'enter your city'}))
    Fullname = forms.CharField(widget=forms.TextInput (attrs={'class':'text-input w-75','placeholder':'enter your fullname'}))
    phone= PhoneFormField()
    country=CountryField()
    Order_Comment =  forms.CharField(widget=forms.Textarea (attrs={'class':'text-input w-100','placeholder':'Enter your comment '}),required=False)
    isDefault = forms.NullBooleanField(widget=forms.CheckboxInput, required=False)
    class Meta:
        model = shippingAdress
        fields = ['address','ZipCode','city','Fullname','phone','country','Order_Comment','isDefault']


class VariantForm (forms.ModelForm):
    Variant = forms.CheckboxInput()
    class Meta:
        model= OrderItem
        fields = ['Variant']



class cantactForm(forms.Form):
    Email = forms.EmailField(widget=forms.TextInput (attrs={'class':'text-input w-75','placeholder':'enter your Email...'}))
    fullname = forms.CharField(max_length=20 ,widget=forms.TextInput (attrs={'class':'text-input w-75','placeholder':'enter your fullname'}))
    feedback = forms.CharField(widget=Textarea (attrs ={'class': 'text-input', 'placeholder':'Enter your feedback ....','style':'height: 150px;'}))

