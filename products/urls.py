from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add, name='product.add'),
    path('edit/<int:i>', views.edit, name='product.edit'),
    path('delete/<int:i>', views.delete, name='product.delete'),
    # path('admin_details/<int:i>', views.admin_details, name='product.admin_details'),
]