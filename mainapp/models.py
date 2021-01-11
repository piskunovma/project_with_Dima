from django.db import models

class CarMarks(models.Model):
    name = models.CharField(verbose_name="Марка авто", max_length=64, unique=True)


class CarModels(models.Model):
    name = models.CharField(verbose_name="Модель авто", max_length=64, unique=True)


class CarYear(models.Model):
    value = models.CharField(verbose_name="Год выпуска", max_length=64, unique=True)


class CarModifications(models.Model):
    value = models.CharField(verbose_name="Комплектация", max_length=64, unique=True)


class CarInfo(models.Model):
    car_mark = models.ForeignKey(CarMarks, verbose_name="Марка авто", on_delete=models.CASCADE)
    car_model = models.ForeignKey(CarModels, verbose_name="Модель авто", on_delete=models.CASCADE)
    car_year = models.ForeignKey(CarYear, verbose_name="Год выпуска авто", on_delete=models.CASCADE)
    car_modification = models.ForeignKey(CarModifications, verbose_name="Модификация(комплектация) авто", on_delete=models.CASCADE)
    # is_default = models.BooleanField(verbose_name="Наличие всех данных по авто" default=False)


class Catalog(models.Model):
    service_name = models.CharField(verbose_name="Название услуги", max_length=64, unique=True)


class CatalogUnique(models.Model):
    catalog = models.ForeignKey(Catalog, verbose_name="Выбранная услуга", on_delete=models.CASCADE)
    carinfo = models.ForeignKey(CarInfo, verbose_name="ID авто", on_delete=models.CASCADE)
    price = models.CharField(verbose_name="Цена услуги", max_length=64)
    decription = models.TextField(verbose_name="Описание услуги", blank=True)

    # def __str__(self):
    #     return self.name