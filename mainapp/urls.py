
from django.urls import path

import mainapp.views as mainapp

app_name = "mainapp"

urlpatterns =[
    path("", mainapp.catalog, name="index"),
    path("basecat/<int:pk>/", mainapp.basecat, name="cat"),
]