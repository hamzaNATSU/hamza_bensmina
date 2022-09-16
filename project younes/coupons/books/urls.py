from django.conf.urls import url
from django.urls import path
from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name= 'booki'

urlpatterns = [
    path('', views.showbooks, name='index'),
    path('home/', views.extractdatafix, name='extractor'),
    path('update_item',views.convertdata , name='update_item'),


]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)