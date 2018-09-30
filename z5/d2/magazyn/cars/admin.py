from django.contrib import admin
from magazyn.cars import Product


class Engine()
class carsAdmin(admin.ModelAdmin):
    list_display = ['name', 'id', 'description', 'is_available']
    search_fields = ['name', 'id']
    list_filter = ['is_available']
    #list_filter2 = ['id']

admin.site.register(Product, ProductAdmin)

# Register your models here.
