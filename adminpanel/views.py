from django.shortcuts import render, redirect
from categories.models import Category
from subcategories.models import Subcategory
from products.models import Product
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm, CustomAuthenticationForm

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


from categories.models import Category
from products.models import Product

@login_required(login_url='admin.login')
def index(request):
    categories_count = Category.objects.count()
    products_count = Product.objects.count()
    users_count = User.objects.count()
    context = {
        'categories_count':categories_count,
        'products_count':products_count,
        'users_count':users_count,
    }
    return render(request, 'adminpanel/index.html', context)

@login_required(login_url='admin.login')
def categories(request):
    categories = Category.objects.all()
    context = {
        'categories':categories
    }
    return render(request, 'adminpanel/categories.html', context)

@login_required(login_url='admin.login')
def subcategories(request):
    categories = Subcategory.objects.all()
    context = {
        'categories':categories
    }
    return render(request, 'adminpanel/subcategories.html', context)

@login_required(login_url='admin.login')
def products(request):
    products = Product.objects.all()
    context = {
        'products':products
    }
    return render(request, 'adminpanel/products.html', context)

@login_required(login_url='admin.login')
def users(request):
    users = User.objects.all()
    context = {
        'users':users
    }
    return render(request, 'adminpanel/users.html', context)

def login_req(request):
    if request.method == "POST":
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_superuser:
                    login(request, user)
                    return redirect("admin.home")
                else:
                    messages.error(request,"Not admin user")
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")
    form = CustomAuthenticationForm()
    return render(request, 'adminpanel/auth/login.html', {'form':form})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("admin.login")


# 65122827
@login_required(login_url='admin.login')
def add_user(request):
    form = CustomUserCreationForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('admin.users')
    return render (request,'adminpanel/auth/add.html', {'form':form})

@login_required(login_url='admin.login')
def edit_user(request,i):
    user = User.objects.get(id=i)
    form = CustomUserCreationForm(request.POST or None, instance=user)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('admin.users')
    return render (request,'adminpanel/auth/edit.html', {'form':form})

@login_required(login_url='admin.login')
def delete_user(request,i):
    user = User.objects.get(id=i)
    user.delete()
    return redirect('admin.users')