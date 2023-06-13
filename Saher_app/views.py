from django.shortcuts import render, redirect
from categories.models import Category
from subcategories.models import Subcategory
from feedbacks.forms import FeedbackForm

def index(request):
    categories = Category.objects.all()
    subcategories = Subcategory.objects.all()
    context = {
        'categories':categories,
        'subcategories':subcategories
    }
    return render (request, 'index.html', context)


def contact(request):
    categories = Category.objects.all()
    subcategories = Subcategory.objects.all()
    form = FeedbackForm(request.POST or None)
    if request.method =='POST':
        if form.is_valid():
            form.save()
            return redirect('main.contact')
    
    context = {
        'categories':categories,
        'subcategories':subcategories,
        'form': form
    }
    return render (request, 'contact.html',context)