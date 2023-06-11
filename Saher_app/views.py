from django.shortcuts import render, redirect
from categories.models import Category
from subcategories.models import Subcategory

def index(request):
    categories = Category.objects.all()
    subcategories = Subcategory.objects.all()
    context = {
        'categories':categories,
        'subcategories':subcategories
    }
    return render (request, 'index.html', context)