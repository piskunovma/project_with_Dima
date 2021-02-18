
from django.urls import path

import mainapp.views as mainapp

app_name = "mainapp"

urlpatterns =[
    path("", mainapp.catalog, name="index"),
    path("marks/", mainapp.carmarks, name="marks"),
    path("models/", mainapp.carmodels, name="models"),
    path("result_catalog/", mainapp.basecat, name="basecat"),
]