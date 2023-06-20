from django.db import models
from subcategories.models import Subcategory


class Product(models.Model):
    name = models.CharField(max_length=50)
    subcategory = models.ForeignKey(
        Subcategory, on_delete=models.CASCADE, related_name='products')
    image = models.ImageField(upload_to='products/')
    price_old = models.DecimalField(
        max_digits=8, decimal_places=2, blank=True, null=True)
    price_new = models.DecimalField(max_digits=8, decimal_places=2)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
