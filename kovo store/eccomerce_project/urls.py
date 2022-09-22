"""eccomerce_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from re import I
from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from product import views as view
from accounts import views
from payment import views as pay

urlpatterns = [
    path('admin/', admin.site.urls),
    path('chaining/', include('smart_selects.urls')),
    path('home/', include('product.urls' , namespace='home')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('payment/', include('payment.urls',namespace='pay')),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^accounts/login/', views.loginuser ),
    path('accounts/profile/<slug:slug>___Col_<col>', views.Profile_detail, name='profile'),
    path('update_item/',view.updateItem , name='update_item'),
    path('create-checkout-session/', pay.create_checkout_session), # new



] 
urlpatterns+= static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
