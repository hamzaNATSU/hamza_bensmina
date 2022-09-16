from django.contrib import admin
from .models import Reservation,Device, email
# Register your models here.

admin.site.register(Reservation)
admin.site.register(Device)

admin.site.register(email)
