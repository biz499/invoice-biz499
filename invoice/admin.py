from django.contrib import admin
from .models import Size, Product, Price, CompanyDetail, Order, InvoiceItem

class SizeAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
    filter_horizontal = ('size',)

class PriceAdmin(admin.ModelAdmin):
    list_display = ('product', 'size', 'price')
    search_fields = ('product__title', 'size__title')
    list_filter = ('product', 'size')

class CompanyDetailAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'gst_number', 'state', 'city', 'pan', 'billing_address')
    search_fields = ('company_name', 'gst_number', 'pan', 'city')

class InvoiceItemInline(admin.TabularInline):
    model = InvoiceItem
    extra = 1
    readonly_fields = ('get_price',)  # Updated to use the method

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'company')
    search_fields = ('company__company_name',)
    inlines = [InvoiceItemInline]

admin.site.register(Size, SizeAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Price, PriceAdmin)
admin.site.register(CompanyDetail, CompanyDetailAdmin)
admin.site.register(Order, OrderAdmin)
