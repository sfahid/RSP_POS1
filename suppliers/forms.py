from django import forms
from .models import Supplier

class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ['name', 'address', 'city', 'state', 'country', 'post_code', 'contact_number', 'email']
