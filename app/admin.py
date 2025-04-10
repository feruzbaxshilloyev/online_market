from django.contrib import admin
from .models import Product, Xabar


# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'desc', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_filter = ('created_at',)


class XabarAdmin(admin.ModelAdmin):
    list_display = ('author', 'is_view', 'created_at', 'desc')
    search_fields = ('author', 'desc')


admin.site.register(Product, ProductAdmin)
admin.site.register(Xabar, XabarAdmin)
