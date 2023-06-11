from django.shortcuts import render, redirect
from .forms import CategoryForm
from .models import Category

def add(request):
    form = CategoryForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('admin.categories')
    return render (request,'categories/add.html', {'form':form})

def edit(request,i):
    category = Category.objects.get(id=i)
    form = CategoryForm(request.POST or None, instance=category)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('admin.categories')
    return render (request,'categories/edit.html', {'form':form})

def delete(request,i):
    category = Category.objects.get(id=i)
    category.delete()
    return redirect('admin.categories')
