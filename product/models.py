from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=150)
    desc = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    category = models.CharField(max_length=150)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    date_published = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
