from django.shortcuts import render, redirect, HttpResponseRedirect
from django.urls import reverse 
from categories.models import Category
from subcategories.models import Subcategory
from feedbacks.forms import FeedbackForm
from products.models import Product

from cards.models import Cart, CartItem

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as lgin
from django.contrib.auth import logout as lgout
from django.contrib.auth import authenticate

from customers.forms import CustomAuthenticationForm, CustomUserCreationForm
from django.contrib import messages


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
    quantity = 0
    if request.user is not None:
        cart = Cart.objects.get(user=request.user)
        quantity = cart.checkproduct(product)
    context = {
        'product': product,
        'quantity': quantity
    }
    return render(request, 'product_details.html', context)



def login(request):
    if request.method == "POST":
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                lgin(request, user)
                return redirect("main.home")
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")
    form = CustomAuthenticationForm()
    return render(request, 'auth/login.html', {'form':form})

def register(request):
    form = CustomUserCreationForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user = form.save()
            lgin(request, user)
            return redirect('main.home')
    return render(request, 'auth/register.html', {'form':form})

def logout(request):
    lgout(request)
    return redirect('main.home')

def addcart(request,i):
    product = Product.objects.get(id=i)
    cart, created = Cart.objects.get_or_create(user = request.user)
    cartitem, created = CartItem.objects.get_or_create(cart = cart, product = product)
    cartitem.quantity+=1
    cartitem.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

def removecart(request,i):
    product = Product.objects.get(id=i)
    cart, created = Cart.objects.get_or_create(user = request.user)
    cartitem, created = CartItem.objects.get_or_create(cart = cart, product = product)
    cartitem.quantity-=1
    cartitem.save()
    if cartitem.quantity == 0:
        cartitem.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

def deletecart(request,i):
    product = Product.objects.get(id=i)
    cart, created = Cart.objects.get_or_create(user = request.user)
    cartitem, created = CartItem.objects.get_or_create(cart = cart, product = product)
    cartitem.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

