from django.contrib import admin
from .models import CarMarks, CarModels, CarYear, CarModifications, CarInfo, Catalog, CatalogUnique, Category, Contact

admin.site.register(CarMarks)
admin.site.register(CarModels)
admin.site.register(CarYear)
admin.site.register(CarModifications)
admin.site.register(CarInfo)
admin.site.register(Catalog)
admin.site.register(CatalogUnique)
admin.site.register(Category)
admin.site.register(Contact)