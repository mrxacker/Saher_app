from django.db import models
from django.contrib.auth.models import User
from products.models import Product

# Create your models here.


class Cart(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='carts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)

    def itemcount(self):
        return self.items.count()

    def totalsum(self):
        total = 0
        for i in self.items.all():
            total += i.total_price()
        return total

    def shipping(self):
        if self.totalsum() < 150:
            return 10
        else:
            return 0

    def total_cost(self):
        return self.totalsum() + self.shipping()

    def checkproduct(self, product):
        quantity = 0
        for i in self.items.all():
            if i.product == product:
                quantity = i.quantity
        return quantity


class CartItem(models.Model):
    cart = models.ForeignKey(
        Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='carts')
    quantity = models.PositiveIntegerField(default=0)

    def total_price(self):
        return self.quantity * self.product.price_new

    def total_price_old(self):
        if self.product.price_old is not None:
            return self.quantity * self.product.price_old
        else:
            return None
