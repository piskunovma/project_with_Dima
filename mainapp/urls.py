
from django.urls import include, path


import mainapp.views as mainapp

app_name = "mainapp"

urlpatterns =[
    path("", mainapp.catalog, name="index"),
    path("<int:product_pk>/", include([
        path("", mainapp.carmarks, name="marks"),
        path("marks/<int:mark_pk>/models/", include([
            path("", mainapp.carmodels, name="models"),
            path("<int:model_pk>/result_catalog/", mainapp.basecat, name="basecat"),
            # path("<int:pk>result_catalog/", mainapp.basecat, name="basecat"),
        ]))        
    ]))
]