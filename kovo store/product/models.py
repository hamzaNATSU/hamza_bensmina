from django.db import models
from django.db.models.deletion import SET_DEFAULT
from django.db.models.fields.related import ForeignKey, create_many_to_many_intermediary_model
from django.utils.translation import ugettext_lazy as _
from ckeditor.fields import RichTextField
from accounts.models import Profile
from settings.models import Variant 


# Create your models here.
class product(models.Model):
    PRDName = models.CharField(max_length=30, verbose_name='Product Name')
    PRDCat = models.ForeignKey('PRD_Cat' , on_delete=models.CASCADE ,limit_choices_to={'PRDCat_Parent__isnull': False}, null=True , related_name='PRDCategory')
    PRDDesc = RichTextField(null = True , blank=True , verbose_name=_('Product Description'))
    PRDPrice = models.DecimalField(max_digits=6, decimal_places=2,verbose_name=_('Product Price'))
    PRDCost = models.DecimalField(max_digits=5 , decimal_places=2, verbose_name=_('Product Cost'), default='0.00')
    PRDBrand = models.ManyToManyField('settings.brand', null=True , blank=True,verbose_name=_("product's Brand")) 
    PRDVariant = models.ManyToManyField('settings.Variant', null=True , blank=True , verbose_name=_("product's Variant")) 
    # PRDCreated = models.DateTimeField(verbose_name=_('created at'), null=True , blank=True)
    PRDImg = models.ImageField(upload_to='products/', null='product/buy-1.jpg', verbose_name=_("product's image"))
    isinstock= models.BooleanField(default=True, verbose_name=_('is in stock'))
    PRDALT = models.ManyToManyField('self',null=True,blank=True, related_name='Alternatives_products', verbose_name='Alternatives')
    PRDACSS = models.ManyToManyField('self',null=True,blank=True, related_name='Accessories_products', verbose_name='Accessories')


    class Meta: 
        verbose_name = ('Product')
        verbose_name_plural = ('Products')
        ordering = ['-id']


    def __str__(self):
        return self.PRDName 


class PRD_Img(models.Model):
    PRDSelected = models.ForeignKey(product, on_delete=models.CASCADE , verbose_name=_('Select Product'))
    PRDImg = models.ImageField(upload_to='product/', verbose_name=_('Product Image 1'), null=True , blank=True)
    PRDImg2 = models.ImageField(upload_to='product/', verbose_name=_('Product Image 2') , null=True , blank= True)
    PRDImg3 = models.ImageField(upload_to='product/', verbose_name=_('Product Image 3') , null=True , blank=True)
    
    class Meta: 
        verbose_name = ('Product Image')
        verbose_name_plural = ('Product Images')

    def __str__(self):
        return str(self.PRDSelected)


class PRD_Cat(models.Model):
    PRDCat = models.CharField(max_length= 30, verbose_name=_('Categorie name'))
    PRDCat_Parent = models.ForeignKey('self',limit_choices_to={  "PRDCat_Parent__isnull" : True} , on_delete=models.CASCADE, blank=True , null=True,verbose_name='main category' ) 
    PRDCat_img = models.ImageField(upload_to='categories', verbose_name=_('Categorie image'), null=True , blank=True)
    class Meta: 
        verbose_name = ('Category') 
        verbose_name_plural = ('Categories')

    def __str__(self) -> str:
        return str(self.PRDCat)

class Deal(models.Model):
    DLName = models.TextField(null= True , blank= True)
    DlImg = models.ImageField(upload_to='deals/', verbose_name=_('Deal Image'),null = True , blank= True)
    class Meta: 
        verbose_name = ('Deal')
        verbose_name_plural = ('Deals')
    
    def __str__(self) -> str:
        return str(self.DLName)

class Orders(models.Model):
    Profile = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True , blank=True)
    dateOrdered= models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100 , null=True)
    paiment_type = models.CharField(max_length=14,null=True , blank=True)
    delivred = models.BooleanField(default=False)
    def __str__(self) -> str:
        return str(self.Profile)+'|'+str(self.transaction_id)

    @property
    def getCart_total(self):
        orderItems = self.orderitem_set.all()
        total = sum([item.getTotal for item in orderItems])
        return total
    @property
    def getdelivery(self):
        delivery = self.getCart_total * 15/100 
        return delivery
    @property
    def get_total(self):
        Total = self.getCart_total + self.getdelivery
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
    Variant = models.ForeignKey('settings.Variant', on_delete=models.CASCADE , null=True , blank=True)
    AddAt = models.DateTimeField(auto_now_add=True)

    @property
    def getTotal(self):
        total = self.product.PRDPrice * self.quantity
        return total


from phone_field import PhoneField
from django_countries.fields import Country, CountryField

class shippingAdress(models.Model):
    costumer= models.ForeignKey(Profile,on_delete=models.SET_NULL,null=True)
    order=models.ForeignKey(Orders, on_delete=models.SET_NULL,null=True)
    country = CountryField(default ='morocco')
    address = models.CharField(max_length=150, null=True , blank=True )
    city = models.CharField(max_length=30,null=True, blank=True)
    phone = PhoneField(blank=True, help_text='Contact phone number')
    ZipCode = models.CharField(null=True , blank = True,max_length=10)
    isDefault = models.BooleanField(default = False , null=True , blank=True)
    Order_Comment = models.TextField(null= True , blank=True, max_length=300)
    Fullname = models.CharField(max_length=30, default='costumer.fullname')


class PrdRvd(models.Model):
    costumer = models.ForeignKey(Profile,on_delete=models.SET_NULL, null=True)
    Product = models.ForeignKey(product,on_delete=models.SET_NULL, null=True)
        



class PrdFvt(models.Model):
    costumer = models.ForeignKey(Profile,on_delete=models.SET_NULL, null=True)
    Product = models.ForeignKey(product,on_delete=models.SET_NULL, null=True)
    
