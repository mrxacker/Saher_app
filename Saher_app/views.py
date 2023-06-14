from django.shortcuts import render, redirect
from categories.models import Category
from subcategories.models import Subcategory
from feedbacks.forms import FeedbackForm


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


def subcategory(request, i):
    subcat = Subcategory.objects.get(id=i)
    context = {
        'subcat': subcat
    }
    return render(request, 'shop.html', context)
