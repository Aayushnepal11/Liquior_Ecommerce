from django.db import models
from pathlib import Path

# Create your models here.


class FeaturedProducts(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(blank=True, null=True, upload_to=('assets/img'))
    description = models.TextField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Featured Product'

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Contact'
        