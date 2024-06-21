from django.contrib import admin
from .models import Product
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display    = ('name', 'description', 'quantity', 'price')
    search_fields   = ('name', 'description')
    readonly_fields = ()
    
admin.site.register(Product, ProductAdmin)