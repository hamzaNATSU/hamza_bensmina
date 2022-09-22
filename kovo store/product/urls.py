from django.conf.urls import url
from product.models import product
from django.urls import path
from django.conf.urls import url
from . import views

app_name= 'product'

urlpatterns = [
    path('', views.product_list, name='index'),
    path('product_<id>',views.product_detail ,name='product'),
    path('shopproducts-<Cat>',views.productfilter , name='shop'),
    path('Cart',views.Cart , name='Cart'),
    path('checkout_order',views.checkout , name='checkout'),
    path('order_process_<transaction_id>',views.orderprocess , name='order_process'),
    path('checkout_2',views.checkout_2 , name='checkout_2'),
    path('infos',views.msginfos , name='infos'),
    path('wishlist',views.favorites , name='wishlist'),
    path('cantact_us',views.cantact_us , name='cantact'),
    path('about_us',views.about_us , name='about_us'),



]