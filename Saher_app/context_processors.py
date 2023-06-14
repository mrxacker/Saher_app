from categories.models import Category
from subcategories.models import Subcategory


def include_categories(request):
    categories = Category.objects.all()
    subcategories = Subcategory.objects.all()

    return {
        'categories': categories,
        'subcategories': subcategories
    }
