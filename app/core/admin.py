from django.contrib import admin

from .models import MenuItem
from .models import Customer
from .models import Table
from .models import Order
from .models import Menu
from .models import Image
from .models import Review


class ImageAdmin(admin.TabularInline):
    model = Image


class MenuItemAdmin(admin.ModelAdmin):
    inlines = [ImageAdmin, ]


# Register your models here.
admin.site.register(MenuItem, MenuItemAdmin)
admin.site.register(Customer)
admin.site.register(Table)
admin.site.register(Order)
admin.site.register(Menu)
admin.site.register(Review)

