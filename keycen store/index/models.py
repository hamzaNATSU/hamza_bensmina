from django.db import models
from django.db.models.deletion import SET_DEFAULT
from django.db.models.fields.related import ForeignKey, create_many_to_many_intermediary_model
from django.utils.translation import ugettext_lazy as _
from ckeditor.fields import RichTextField
# Create your models here.



# Create your models here.
class product(models.Model):
    PRDName = models.CharField(max_length=30, verbose_name='Product Name')
    PRDDesc = RichTextField(null = True , blank=True , verbose_name=_('Product Description'))
    PRDPrice = models.DecimalField(max_digits=6, decimal_places=2,verbose_name=_('Product Price'))
    PRDCost = models.DecimalField(max_digits=5 , decimal_places=2, verbose_name=_('Product Cost'), default='0.00')
    # PRDCreated = models.DateTimeField(verbose_name=_('created at'), null=True , blank=True)
    PRDImg = models.ImageField(upload_to='products/', null='product/buy-1.jpg', verbose_name=_("product's image"))
    isinstock= models.BooleanField(default=True, verbose_name=_('is in stock'))
    PRDALT = models.ManyToManyField('self',null=True,blank=True, related_name='Alternatives_products', verbose_name='Alternatives')
    variant = models.ManyToManyField('Variant',null=True,blank=True, related_name='variant', verbose_name='variant')
   

    class Meta: 
        verbose_name = ('Product')
        verbose_name_plural = ('Products')
        ordering = ['-id']
    def __str__(self):
        return self.PRDName 

class Variant(models.Model):
    VRTtitle = models.CharField(max_length=40, verbose_name='variant')
    def __str__(self):
        return self.VRTtitle 


class guestcostumer(models.Model):
    device_id = models.CharField(max_length=50,verbose_name='device_id')
    email_costumer = models.CharField(max_length=30, verbose_name='costumer email')


class Orders(models.Model):
    costumer= models.ForeignKey(guestcostumer,on_delete=models.SET_NULL, null=True , blank=True) 
    dateOrdered= models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100 , null=True)
    delivred = models.BooleanField(default=False)
    def __str__(self) -> str:
        return str(self.costumer.id)+'|'+str(self.transaction_id)
    @property
    def getCart_total(self):
        orderItems = self.orderitem_set.all()
        total = sum([item.getTotal for item in orderItems])
        return total
    @property
    def get_total(self):
        Total = self.getCart_total
        return Total    
    @property
    def get_itemstotal(self):
        orderItems = self.orderitem_set.all()
        items = sum(item.quantity for item in orderItems)
        return items 

class OrderItem(models.Model):
    product=models.ForeignKey(product, on_delete=models.SET_NULL,null=True)
    Order=models.ForeignKey(Orders, on_delete=models.SET_NULL,null=True)
    quantity = models.IntegerField(default=0 , null=True , blank=True)
    Variant = models.CharField(max_length=40,null=True , blank=True)
    AddAt = models.DateTimeField(auto_now_add=True)

    @property
    def getTotal(self):
        total = self.product.PRDPrice * self.quantity
        return total
