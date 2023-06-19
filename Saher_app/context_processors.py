from categories.models import Category
from subcategories.models import Subcategory
from cards.models import Cart


def include_categories(request):
    categories = Category.objects.all()
    subcategories = Subcategory.objects.all()
    shopping_cart, created =  Cart.objects.get_or_create(user = request.user, status = False)

    return {
        'categories': categories,
        'subcategories': subcategories,
        'shopping_cart': shopping_cart,
    }
