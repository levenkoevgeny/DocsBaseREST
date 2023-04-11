from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser, Region, Subdivision, CategoryItem, DocData


class CustomUserAdmin(UserAdmin):
    pass


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Region)
admin.site.register(Subdivision)
admin.site.register(CategoryItem)
admin.site.register(DocData)
