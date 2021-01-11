from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

import mainapp.views as mainapp

urlpatterns =[
    path("admin/", admin.site.urls),
    path("", mainapp.main, name="main"),
    path("catalog/", mainapp.catalog, name="catalog"),
    path("contacts/", mainapp.contacts, name="contacts"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)