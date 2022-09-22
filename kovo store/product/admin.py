from django.contrib import admin 
from .models import Deal, OrderItem, Orders, PRD_Cat, PRD_Img, PrdFvt, PrdRvd, product, shippingAdress

# Register your models here.

admin.site.register(product)
admin.site.register(PRD_Img)
admin.site.register(PRD_Cat)
admin.site.register(Deal)
admin.site.register(OrderItem)
admin.site.register(Orders)
admin.site.register(shippingAdress)
admin.site.register(PrdFvt)
admin.site.register(PrdRvd)
