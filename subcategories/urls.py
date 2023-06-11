from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add, name='subcategory.add'),
    path('edit/<int:i>', views.edit, name='subcategory.edit'),
    path('delete/<int:i>', views.delete, name='subcategory.delete'),
]
