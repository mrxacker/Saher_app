from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)
    icon = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name