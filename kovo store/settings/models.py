from django.db import models
from django.db.models.fields import CharField
from django.utils.translation import ugettext_lazy as _
# Create your models here.

class brand(models.Model):
    BRDName = models.CharField(max_length=15 , verbose_name=_('Brand name'))
    BRRDescription = models.TextField(blank=True , null=True, verbose_name=_('Brand description'))
    class Meta: 
        verbose_name =_('brand')
        verbose_name_plural =_('brands')

    def __str__(self) -> str:
        return self.BRDName
        
        
class Variant(models.Model):
    VRTName = models.CharField(max_length=15, verbose_name=_('Variant name'))
    VRTescription = models.TextField(blank=True , null=True, verbose_name=_('Variant description'))
    class Meta: 
        verbose_name =_('Variant')
        verbose_name_plural =_('Variants')

    def __str__(self) -> str:
        return self.VRTName
        
class INTAds(models.Model):
    INTAName = models.CharField(max_length=15, verbose_name=_('Ad name'))
    INTADate = models.DateField(blank=True , null=True, verbose_name=_('Added at:'))
    INTAImg = models.ImageField(upload_to='Ads_images/', blank=True , null= True)
    class Meta: 
        verbose_name =_('intern Ad')
        verbose_name_plural =_('intern Ads')

    def __str__(self) -> str:
        return self.INTAName
        
class Collection(models.Model):
    CLTName = models.CharField(max_length=15, verbose_name=_('Collection Title (part1) '))
    CLTName2 = models.CharField(max_length=15, verbose_name=_('Collection Title(part 2) '))
    CLTDesc = models.TextField(blank=True , null=True, verbose_name=_('description:'))
    CLTImg = models.ImageField(upload_to='Clts_images/', blank=True , null= True)
    class Meta: 
        verbose_name =_('Collection')
        verbose_name_plural =_('Collections')

    def __str__(self) -> str:
        return self.CLTName
