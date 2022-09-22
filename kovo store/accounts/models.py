from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model
from django.db.models.fields import EmailField
from django.db.models.fields.related import ForeignKey
from django_countries.fields import Country, CountryField
import datetime
from django.utils.text import slugify
from django.db.models.signals import post_save
from phone_field import PhoneField
from address.models import AddressField
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, verbose_name='user', on_delete=models.CASCADE)
    slug = models.SlugField(null=True , blank=True)
    image = models.ImageField(verbose_name="avatar" , upload_to='profile/img', null=True , blank=True)
    join_date = models.DateTimeField(verbose_name="joined at" , default=datetime.datetime.now)
    fullname = models.CharField(verbose_name="full name", max_length=20 , null=True , blank=True)
    phone = PhoneField(blank=True, help_text='Contact phone number')
    country = CountryField()
    address = models.CharField(max_length=150, null=True , blank=True )
    city = models.CharField(max_length=30,null=True, blank=True)
    ZipCode = models.CharField(null=True , blank = True,max_length=10)
    class Meta:
        verbose_name=('Profile')
        verbose_name_plural=('Profiles')

    def save(self , *args , **kwargs):
        if not self.slug :
            self.slug = slugify(self.user.username)
        super(Profile , self).save(*args,**kwargs)


    def __str__(self) -> str:
        return '%s' %(self.user)
    

    def get_absolute_url(self):
        return reversed("Profile_detail", kwargs={"pk" , self.pk})




class Email(models.Model):
    costumer = ForeignKey(Profile,on_delete=models.CASCADE)
    Email_text = EmailField(null=True , blank=True)
    def __str__(self) -> str:
        return str(self.costumer)