from django.db import models
from cards.models import Cart

class Order(models.Model):
    payment_type = models.CharField(max_length=30)
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    note = models.CharField(max_length=200)
    cart = models.OneToOneField(Cart,on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

