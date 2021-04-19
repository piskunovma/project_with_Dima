from django.conf import settings
from django.shortcuts import render
from django.utils import timezone

from variables import TEST
from .models import Catalog, Category, Contact, CarMarks, CarModels

def main(request):
    title = 'Главная'
    products = Category.objects.all()
    content = {"title": title, "products": products, "media_url": settings.MEDIA_URL}
    return render(request, "mainapp/index.html", content)

def catalog(request):
    title = 'Каталог'
    products = Catalog.objects.all()
    content = {"title": title, "products": products, "media_url": settings.MEDIA_URL}
    return render(request, "mainapp/catalog.html", content)

def carmarks(request, product_pk):
    title = "Марки машин"
    marks = CarMarks.objects.all()
    content = {"title":title, "marks":marks, "media_url": settings.MEDIA_URL, "product_pk":product_pk}
    return render(request, "mainapp/carmarks.html", content)

def carmodels(request, product_pk, mark_pk):
    title = "Модели машин"
    models = CarModels.objects.all()
    content = {"title":title, "models":models, "media_url": settings.MEDIA_URL, "product_pk":product_pk, "mark_pk":mark_pk}
    return render(request, "mainapp/carmodels.html", content)

def basecat(request, product_pk, mark_pk, model_pk):
    title = "Итоговый каталог"
    """[pk-1].service_name"""
    product = Catalog.objects.all().filter(pk = product_pk)[0]
    content = {"title":title, "product": product}
    return render(request, "mainapp/base_cat.html", content)


def contact(request):
    title = "о нас"
    visit_date = timezone.now()
    locations = Contact.objects.all()
    content = {"title": title, "visit_date": visit_date, "locations": locations}
    return render(request, "mainapp/contacts.html", content)
    