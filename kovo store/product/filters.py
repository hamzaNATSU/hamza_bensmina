from typing import ClassVar
from django.db.models.expressions import Value
from django.db.models.fields import CharField
from django.db.models.query import QuerySet
from django.forms.widgets import Widget
from settings.models import brand
from django_filters import FilterSet
import django_filters
from django_filters.filters import ModelMultipleChoiceFilter, RangeFilter
from .models import product
from settings.models import brand
# from .forms import multi
from .widgets import CustomRangeWidget
from django import forms
from django.forms import CheckboxSelectMultiple

class AllRangeFilter(RangeFilter):
    def __init__ (self, *args, **kwargs):
        super(). __init__ (*args, **kwargs)
        values = [ int(p.PRDPrice) for p in product.objects.all()]
        min_value = 0
        max_value = 500
        self.extra['widget'] = CustomRangeWidget(attrs={'data-range_min':min_value,'data-range_max':max_value})

class productFilter(FilterSet):
  PRDPrice = AllRangeFilter()

  class Meta:
      model = product
      fields = ['PRDPrice', ]
      # form = ProductFilterFormHelper
      
class searchfilter(FilterSet):
    PRDName= django_filters.CharFilter(label='',lookup_expr='icontains')
    class Meta:
        model = product
        fields = ['PRDName']

def departments(request):
    if request is None:
        return product.objects.none()

    company = request.user.company
    return company.department_set.all()

class brandfilter(django_filters.FilterSet):
    PRDBrand = ModelMultipleChoiceFilter(widget=forms.CheckboxSelectMultiple,queryset=(brand.objects.all()), label="") #hada rah filter li gtlk dyal chkbox
    class Meta:
        model = product
        fields = ['PRDBrand']
