# from django.shortcuts import render, get_object_or_404, redirect
# from .models import Product
# from .forms import ProductForm


from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .models import Product
from .forms import ProductForm
import json

def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_spa.html', {'products': products})

def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'products/product_detail.html', {'product': product})

def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'products/product_form.html', {'form': form})

def product_update(request, id):
    product = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'products/product_form.html', {'form': form})

def product_delete(request, id):
    product = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'products/product_confirm_delete.html', {'product': product})



def product_list_api(request):
    products = Product.objects.all().values('id', 'name', 'description', 'price', 'saleCom', 'purCom','stock')
    return JsonResponse(list(products), safe=False)

def product_detail_api(request, id):
    product = get_object_or_404(Product, id=id)
    return JsonResponse({
        'id': product.id,
        'name': product.name,
        'description': product.description,
        'price': product.price,
        'saleCom' : product.saleCom,
        'purCom' : product.purCom,
        'stock': product.stock,
    })

@csrf_exempt
@require_http_methods(["POST"])
def product_create_api(request):
    data = json.loads(request.body)
    product = Product.objects.create(
        name=data['name'],
        description=data['description'],
        price=data['price'],
        saleCom=data['saleCom'],
        purCom=data['purCom'],
        stock=data['stock']
    )
    return JsonResponse({'id': product.id})

@csrf_exempt
@require_http_methods(["PUT"])
def product_update_api(request, id):
    product = get_object_or_404(Product, id=id)
    data = json.loads(request.body)
    product.name = data['name']
    product.description = data['description']
    product.price = data['price']
    product.saleCom = data['saleCom']
    product.purCom = data['purCom']
    product.stock = data['stock']
    product.save()
    return JsonResponse({'id': product.id})

@csrf_exempt
@require_http_methods(["DELETE"])
def product_delete_api(request, id):
    product = get_object_or_404(Product, id=id)
    product.delete()
    return HttpResponse(status=204)
