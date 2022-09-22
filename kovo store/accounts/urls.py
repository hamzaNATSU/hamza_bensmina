from django.urls import path
from django.conf.urls import url
from . import views

app_name='accounts'


urlpatterns = [
    path('signup/', views.signup, name='signup'), 
    url(r'^login/', views.loginuser, name='login'),
    path('logout/', views.logoutuser, name='logoutuser'), 
]