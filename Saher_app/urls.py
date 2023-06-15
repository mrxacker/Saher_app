"""Saher_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler400

from django.conf import settings
from django.conf.urls.static import static

from . import views


handler400 = views.error400

urlpatterns = [
    path('admin/', admin.site.urls),
    path('categories/', include('categories.urls')),
    path('subcategories/', include('subcategories.urls')),
    path('products/', include('products.urls')),
    path('orders/', include('orders.urls')),
    path('adminpanel/', include('adminpanel.urls')),

    path("", views.index, name="main.home"),
    path("contact/", views.contact, name="main.contact"),

    path('sub/<int:i>', views.subcategory, name='main.sub'),
    path('product/<int:i>', views.product, name='main.product'),

    path('login/', views.login, name='main.login'),
    path('register/', views.register, name='main.register'),
    path('logout/', views.logout, name='main.logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
