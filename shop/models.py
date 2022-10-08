from django.db import models

# Create your models here.


class Featured:
    name = models.CharField(max_length=80)
    description = models.TextField()
    image = models.ImageField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    @property
    def imgURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
