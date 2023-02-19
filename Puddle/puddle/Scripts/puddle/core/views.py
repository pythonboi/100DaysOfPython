# This is your frontEnd for viewing the webpages

from django.shortcuts import render

# import the database to view it on the webpage

from item.models import Category, Item


# Create your views here.

# This will be showing your webpage
def index(request):
    # To show the first 6 item or new 6 times
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()

    return render(request, 'core/index.html', {
        'categories': categories,
        'items': 'items'
    })


def contact(request):
    return render(request, 'core/contact.html')
