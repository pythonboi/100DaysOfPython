
# This model is use for configuring the Django web admin database items
from django.contrib.auth.models import User
from django.db import models


# Create your models here.


# Create a class for item

class Category(models.Model):
    name = models.CharField(max_length=255)

    # Create a class for name ordering of the category and also the spelling in plural form
    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'

    # Create a function for the showing the name you gave to your database category item
    def __str__(self):
        return self.name


class Item(models.Model):
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    image = models.ImageField(upload_to='item_images', blank=True, null=True)
    is_sold = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
