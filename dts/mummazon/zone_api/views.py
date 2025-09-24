from django.shortcuts import render
from django.http import JsonResponse


# Create your views here.

def product_list(request):
    products = [
        {"name": "Headphones", "price": 100, "category": "Electronics"},
        {"name": "Shoes", "price": 80, "category": "Footwear"},
        {"name": "Watch", "price": 150, "category": "Accessories"},
        {"name": "Backpack", "price": 60, "category": "Bags"},
        {"name": "Sunglasses", "price": 120, "category": "Accessories"},
        {"name": "Smartphone", "price": 700, "category": "Electronics"},
        {"name": "Laptop", "price": 1200, "category": "Electronics"},
        {"name": "Jacket", "price": 200, "category": "Clothing"},
        {"name": "Bicycle", "price": 300, "category": "Outdoor"},
        {"name": "Camera", "price": 500, "category": "Electronics"}
    ]
    return JsonResponse(products, safe=False)