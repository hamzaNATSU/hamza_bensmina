from django.conf.urls import url
from django.db import models
from django.db.models.base import Model
from urllib.request import urlopen
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
import urllib
import os
import requests
from django.core.files import File
# Create your models here.

class book(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(max_length=300, blank=True, null=True)
    image_url = models.URLField(blank=True, null=True)
    image = models.ImageField(null= True, blank=True)
    url = models.CharField(max_length=100)

    def get_image_from_url(self):
        if self.image_url and not self.image:
            result = urllib.request.urlretrieve(self.image_url)
            self.image.save(
                os.path.basename(self.image_url),
                File(open(result[0], 'rb'))
                )
        self.save()
    def __str__(self):
        return self.title