from django.shortcuts import render, redirect
from .forms import ProductForm
from .models import Product

def add(request):
    form = ProductForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('admin.products')
    return render (request,'products/add.html', {'form':form})

def edit(request,i):
    product = Product.objects.get(id=i)
    form = ProductForm(request.POST or None, request.FILES or None, instance=product)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('admin.products')
    return render (request,'products/edit.html', {'form':form})

def delete(request,i):
    product = Product.objects.get(id=i)
    product.delete()
    return redirect('admin.products')


# def admin_details(request, i ):
#     product = Product.objects.get(id=i)
#     return render (request,'adminpanel/product_details.html', {'product':product})