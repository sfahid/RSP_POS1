from django.shortcuts import render, get_object_or_404, redirect
from .models import Supplier
from .forms import SupplierForm

def supplier_list(request):
    suppliers = Supplier.objects.all()
    return render(request, 'suppliers/supplier_list.html', {'suppliers': suppliers})

def supplier_detail(request, id):
    supplier = get_object_or_404(Supplier, id=id)
    return render(request, 'suppliers/supplier_detail.html', {'supplier': supplier})

def supplier_create(request):
    if request.method == 'POST':
        form = SupplierForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('supplier_list')
    else:
        form = SupplierForm()
    return render(request, 'suppliers/supplier_form.html', {'form': form})

def supplier_update(request, id):
    supplier = get_object_or_404(Supplier, id=id)
    if request.method == 'POST':
        form = SupplierForm(request.POST, instance=supplier)
        if form.is_valid():
            form.save()
            return redirect('supplier_list')
    else:
        form = SupplierForm(instance=supplier)
    return render(request, 'suppliers/supplier_form.html', {'form': form})

def supplier_delete(request, id):
    supplier = get_object_or_404(Supplier, id=id)
    if request.method == 'POST':
        supplier.delete()
        return redirect('supplier_list')
    return render(request, 'suppliers/supplier_confirm_delete.html', {'supplier': supplier})
