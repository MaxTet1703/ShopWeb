from django.contrib import admin
from .models import *

# Register your models here.

class MenuAdmin(admin.ModelAdmin):
    list_display = ("type_of_position", "name", "price")
    fields = ("type_of_position", "name", "description", "image", "price")


class CategoriesAdmin(admin.ModelAdmin):
    list_display = ("title",)
    fields = ('title',)


admin.site.register(Menu, MenuAdmin)
admin.site.register(Chapter, CategoriesAdmin)