from django.urls import path

from . import views

app_name= 'payment'

urlpatterns = [
    path('', views.HomePageView, name='payment'),
    path('paypalpay/', views.paypalpay, name='paypal'),
    path('on_cash/', views.on_cash, name='on_cash'),
    path('download/', views.download, name='download'),

        ]