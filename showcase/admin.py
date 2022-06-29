from django.contrib import admin
from .models import Menu, VolumeList

# Register your models here.

class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'volume')


admin.site.register(Menu, MenuAdmin)
admin.site.register(VolumeList)
