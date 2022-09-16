from email.policy import default
from turtle import pos
from unittest.mock import DEFAULT
from django.db import models
import datetime
from django.db.models.signals import post_save,post_delete
# Create your models here.


class Device(models.Model):
    IDDev = models.CharField(max_length=20,null=True,blank=True)
    brand = models.CharField(max_length=20,null=True,blank=True)
    SerialDev = models.CharField(max_length=20,null=True,blank=True)
    typeDev = models.CharField(max_length=20,null=True,blank=True)
    Reserved = models.BooleanField(default=False)
    def __str__(self) -> str:
        if self.IDDev==None:
            return "ERROR-CUSTOMER NAME IS NULL"
        return self.IDDev

class Reservation(models.Model):
    IDStud = models.CharField(max_length=20,null=True,blank=True)
    NameStud = models.CharField(max_length=20,null=True,blank=True)
    Device = models.ForeignKey("Device", verbose_name=("device"), on_delete=models.CASCADE)
    DateRes = models.DateTimeField(default=datetime.datetime.today())
    DateExp = models.DateTimeField(null=True,blank=True)
    Ended = models.BooleanField(default=False)
    def __str__(self) -> str:
        return self.IDStud


def save_profile(sender, instance, **kwargs):
    Device.objects.filter(id = instance.Device.id).update(Reserved=True)
    # Reservation.objects.filter(id = instance.id).update(DateExp = instance.DateRes + datetime.timedelta(days=instance.Duration))

def update_device(sender,instance, **kwargs):
    Device.objects.filter(id = instance.Device.id).update(Reserved=False)
post_save.connect(save_profile, sender=Reservation)
post_delete.connect(update_device, sender=Reservation)


class email(models.Model):
    Eemail = models.EmailField(max_length=254,null=True,blank=True)
