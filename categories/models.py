from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)
    icon = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    def products(self):
        all_products=[]
        for subcategory in self.subcategories.all():
            for product in subcategory.products.all().order_by('created_at'):
                all_products.append(product)
        return all_products