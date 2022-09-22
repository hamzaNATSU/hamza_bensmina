from django.contrib import admin
from .models import Collection, brand,Variant,INTAds
# Register your models here.

admin.site.register(brand)
admin.site.register(Variant)
admin.site.register(INTAds)
admin.site.register(Collection)