from django.conf import settings
from django.shortcuts import render
from django.utils import timezone

from .models import Catalog, Category, Contact

def main(request):
    title = 'Главная'
    products = Category.objects.all()

    content = {"title": title, "products": products, "media_url": settings.MEDIA_URL}
    return render(request, "mainapp/index.html", content)

def catalog(request, pk=None):
    title = 'Каталог'
    products = Catalog.objects.all()

    content = {"title": title, "products": products, "media_url": settings.MEDIA_URL}
    if pk:
        print(f"User select category: {pk}")
    return render(request, "mainapp/catalog.html", content)

def contact(request):
    title = "о нас"
    visit_date = timezone.now()
    locations = Contact.objects.all()
    content = {"title": title, "visit_date": visit_date, "locations": locations}
    return render(request, "mainapp/contacts.html", content)