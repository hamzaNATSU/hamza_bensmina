from os import name
from django.conf.urls import url
from django.urls import path
from .views import index, thankYou,updateItem,checkout,sendorder

app_name='index'

urlpatterns = [
    path('', index, name='home'),
    path('update_item/', updateItem, name='update_item'),
    path('checkout/', checkout, name='checkout'),
    path('transaction_ended_<transaction_id>',sendorder, name='transaction_end'),
    path('order_confirmation_<transaction_id>',thankYou,name='comfirmed')
]