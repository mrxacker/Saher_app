from django.shortcuts import render, redirect
from .forms import SubcategoryForm
from .models import Subcategory

def add(request):
    form = SubcategoryForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('admin.subcategories')
    return render (request,'subcategories/add.html', {'form':form})

def edit(request,i):
    category = Subcategory.objects.get(id=i)
    form = SubcategoryForm(request.POST or None, instance=category)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('admin.subcategories')
    return render (request,'subcategories/edit.html', {'form':form})

def delete(request,i):
    category = Subcategory.objects.get(id=i)
    category.delete()
    return redirect('admin.subcategories')

