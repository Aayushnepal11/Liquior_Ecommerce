from django.db import models
from django.urls import reverse


# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Contact'


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('store:product_list_by_category', args=[self.slug])


# You should use all models on small letters others wise field error will arise.
class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    price = models.IntegerField()
    image = models.ImageField(upload_to='products')
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''

        return url

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'
        index_together = (('id', 'slug'),)

    """
    def get_absolute_url(self):
        return reverse('store:product_detail', args=[self.id, self.slug])
    """

    def __str__(self):
        return self.name
