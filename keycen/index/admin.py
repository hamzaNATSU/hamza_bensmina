from django.contrib import admin
from .models import OrderItem, Orders, Variant, guestcostumer, product
# Register your models here.
admin.site.register(product)
admin.site.register(Variant)
admin.site.register(guestcostumer)
admin.site.register(Orders)
admin.site.register(OrderItem)