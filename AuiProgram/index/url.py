
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name= 'aui'

urlpatterns = [
    path('', views.index, name='index'),
    path('reserve', views.Reserve, name='Reserve'),
    path('Add_device',views.AddDevice,name='AddDevice'),
    path('alert',views.updatealerts,name='alert'),
    path('change_email',views.changeemail,name='changeemail'),
    path('Reservation_<id>_Details_<type>',views.ResDetails,name='ResDetails'),
    path('confirmation_<mail>',views.confirmmail,name='confirmemail'),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)