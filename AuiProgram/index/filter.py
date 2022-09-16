      
import genericpath
import imp
from django_filters import FilterSet,OrderingFilter
import django_filters
from django.db.models import Q


from .models import Reservation,Device


class searchfilter(FilterSet):
    q= django_filters.CharFilter(method='my_custom_filter' , label='')
    class Meta:
        model = Reservation
        fields = ['q']

    def my_custom_filter(self, queryset, name, value):
        return Reservation.objects.filter( Q(NameStud__icontains=value) | Q(IDStud__icontains=value) | Q(Device__IDDev =value))