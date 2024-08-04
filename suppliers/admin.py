from django.contrib import admin
from .models import Supplier

class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'city', 'state', 'country', 'post_code', 'contact_number', 'email', 'created_at', 'updated_at')
    search_fields = ('name', 'city', 'state', 'country')
    list_filter = ('created_at', 'updated_at')

admin.site.register(Supplier, SupplierAdmin)
