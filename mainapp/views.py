from django.shortcuts import render
import datetime

def main(request):
    title = 'Главная'
    products = [
        {
            'name': 'Шины',
            'desc': 'Новые',
            'image_src': 'tires.jpg',
            'image_href': '/product/1/',
            'alt': 'продукт 1',
        },
        {
            'name': 'Двигатель',
            'desc': 'Ремонт Двигателя',
            'image_src': 'dvigatel.jpg',
            'image_href': '/product/2/',
            'alt': 'продукт 2',
        },
        {
            'name': 'Масло',
            'desc': 'Моторное',
            'image_src': 'oil.jpg',
            'image_href': '/product/3/',
            'alt': 'продукт 3',
        },
        {
            'name': 'КПП',
            'desc': 'Коробка передач ремонт',
            'image_src': 'dsg7_KPP.jpg',
            'image_href': '/product/4/',
            'alt': 'продукт 4',
        },
        {
            'name': 'Диагностика',
            'desc': 'Компьютерная',
            'image_src': 'diagnostics.jpg',
            'image_href': '/product/5/',
            'alt': 'продукт 5',
        },
    ]
    content = {"title": title, "products": products}
    return render(request, "mainapp/index.html", content)

def catalog(request):
    title = 'Каталог'
    products = [
        {
            'name': 'Шины',
            'desc': 'Новые',
            'image_src': 'tires.jpg',
            'image_href': '/product/1/',
            'alt': 'продукт 1',
        },
        {
            'name': 'Двигатель',
            'desc': 'Ремонт Двигателя',
            'image_src': 'dvigatel.jpg',
            'image_href': '/product/2/',
            'alt': 'продукт 2',
        },
        {
            'name': 'Масло',
            'desc': 'Моторное',
            'image_src': 'oil.jpg',
            'image_href': '/product/3/',
            'alt': 'продукт 3',
        },
        {
            'name': 'КПП',
            'desc': 'Коробка передач ремонт',
            'image_src': 'dsg7_KPP.jpg',
            'image_href': '/product/4/',
            'alt': 'продукт 4',
        },
        {
            'name': 'Диагностика',
            'desc': 'Компьютерная',
            'image_src': 'diagnostics.jpg',
            'image_href': '/product/5/',
            'alt': 'продукт 5',
        },
         {
            'name': 'Подвеска',
            'desc': 'Ремонт',
            'image_src': 'suspension.jpg',
            'image_href': '/product/6/',
            'alt': 'продукт 6',
        },
    ]
    content = {"title": title, "products": products}
    return render(request, "mainapp/catalog.html", content)

def contacts(request):
    title = "контакты"
    visit_date = datetime.datetime.now()
    locations = [
        {"city": "Москва", "phone": "+7-888-888-8888", "email": "info@geekshop.ru", "address": "В пределах МКАД"},
    ]
    content = {"title": title, "visit_date": visit_date, "locations": locations}
    return render(request, "mainapp/contacts.html", content)