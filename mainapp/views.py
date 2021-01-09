from django.shortcuts import render

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
    return render(request, "mainapp/catalog.html")