from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.login_req, name="admin.login"),
    path("logout/", views.logout_request, name="admin.logout"),
    path('', views.index, name='admin.home'),
    path('categories/', views.categories, name='admin.categories'),
    path('subcategories/', views.subcategories, name='admin.subcategories'),
    path('products/', views.products, name='admin.products'),
    path('users/', views.users, name='admin.users'),
    path('users/add/', views.add_user, name='admin.user.add'),
    path('users/edit/<int:i>', views.edit_user, name='admin.user.edit'),
    path('users/delete/<int:i>', views.delete_user, name='admin.user.delete'),
]
