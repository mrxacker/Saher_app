from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add, name='category.add'),
    path('edit/<int:i>', views.edit, name='category.edit'),
    path('delete/<int:i>', views.delete, name='category.delete'),
]
