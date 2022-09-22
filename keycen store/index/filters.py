      
from django_filters import FilterSet
import django_filters
from .models import product


class searchfilter(FilterSet):
    PRDName= django_filters.CharFilter(label='',lookup_expr='icontains')
    class Meta:
        model = product
        fields = ['PRDName']
