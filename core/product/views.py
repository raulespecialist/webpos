from django.shortcuts import render
from django.http.request import HttpRequest
from django.http import JsonResponse
from django.views import View
from .models import Product


def product_list(request):
    products = Product.objects.all()
    return render(request, 'product/product_list.html', {'products':products})

def search_product(request):
    """everytime user inputs to search box, this function runs"""
    product = request.GET.get("product")
    productlist = []
    if product:
        #collect every objects that contains the input text
        product_objects = Product.objects.filter(title__icontains=product).values()
        for product in product_objects:
            productlist.append(product)
    return JsonResponse({'status':200, 'product':productlist})