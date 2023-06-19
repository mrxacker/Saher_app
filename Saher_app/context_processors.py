from categories.models import Category
from subcategories.models import Subcategory
from cards.models import Cart


def include_categories(request):
    categories = Category.objects.all()
    subcategories = Subcategory.objects.all()
    if request.user.is_authenticated:
        shopping_cart, created =  Cart.objects.get_or_create(user = request.user, status = False)
    else:
        shopping_cart = None

    return {
        'categories': categories,
        'subcategories': subcategories,
        'shopping_cart': shopping_cart,
    }
