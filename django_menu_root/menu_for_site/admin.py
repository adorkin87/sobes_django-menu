from django.contrib import admin
from . import models

class ItemMenuAdmin(admin.ModelAdmin):
    list_display = ('menu', 'name', 'parent', 'url')
    prepopulated_fields = {'url': ('name',)}

admin.site.register(models.Menu)
admin.site.register(models.ItemMenu, ItemMenuAdmin)
