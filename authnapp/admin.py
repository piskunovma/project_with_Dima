from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import ServiceUser


class ServiceUserAdmin(UserAdmin):
    pass


admin.site.register(ServiceUser, ServiceUserAdmin)