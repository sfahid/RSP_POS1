from django.contrib import admin
from .models import Customer

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'address', 'city', 'state', 'country', 'post_code', 'due_amount', 'created_at', 'updated_at')
    search_fields = ('first_name', 'last_name', 'city', 'state', 'country')
    list_filter = ('created_at', 'updated_at')

admin.site.register(Customer, CustomerAdmin)
