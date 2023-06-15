from django.shortcuts import render, redirect
from categories.models import Category
from subcategories.models import Subcategory
from feedbacks.forms import FeedbackForm
from products.models import Product

from customers.forms import CustomerForm


from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as lgin
from django.contrib.auth import logout as lgout
from django.contrib.auth import authenticate


def index(request):
    return render(request, 'index.html')


def error400(request, exception):
    return render(request, '404.html', status=404)


def contact(request):
    form = FeedbackForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('main.contact')

    context = {
        'form': form
    }
    return render(request, 'contact.html', context)

order_options = [
    ('','Default'),
    ('date','Newest'),
    ('price','price: low to high'),
    ('price-desc','price: high to low'),
]

def subcategory(request, i):
    subcat = Subcategory.objects.get(id=i)
    all_products = Product.objects.filter(subcategory = subcat)
    if 'orderby' in request.GET:
        if request.GET['orderby'] == 'date':    
            all_products = Product.objects.filter(subcategory = subcat).order_by('created_at')
        elif request.GET['orderby'] == 'price':
            all_products = Product.objects.filter(subcategory = subcat).order_by('price_new')
        elif request.GET['orderby'] == 'price-desc':
            all_products = Product.objects.filter(subcategory = subcat).order_by('-price_new')
    context = {
        'subcat': subcat,
        'all_products':all_products,
        'select_opt':request.GET['orderby'],
        'order_options':order_options,
    }
    return render(request, 'shop.html', context)

def product(request, i):
    product = Product.objects.get(id=i)
    context = {
        'product': product
    }
    return render(request, 'product_details.html', context)



def login(request):
    pass

def register(request):
    form = CustomerForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            

            return redirect('/')
    return render(request, 'auth/register.html', {'form':form})

def logout(request):
    pass