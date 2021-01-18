from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.conf.urls import include

import mainapp.views as mainapp

urlpatterns =[
    path("admin/", admin.site.urls),
    path("", mainapp.main, name="main"),
    path("catalog/", include("mainapp.urls", namespace="catalog")),
    path("contacts/", mainapp.contact, name="contacts"),
    path("auth/", include("authnapp.urls", namespace="auth")),
    path("carmarks/", mainapp.carmarks, name="carmarks"),
    path("carmodels/", mainapp.carmodels, name="carmodels"),
    path("baseinfo/", mainapp.baseinfo, name="baseinfo"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)