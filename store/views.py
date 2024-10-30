from django.shortcuts import render, get_object_or_404
from .models import Product, Order, Category

def product_list(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    return render(request, 'store/product_list.html', {'products': products, 'categories': categories})

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    categories = Category.objects.all()
    return render(request, 'store/product_detail.html', {'product': product, 'categories': categories})

def order_list(request):
    orders = Order.objects.all()
    categories = Category.objects.all()
    return render(request, 'store/order_list.html', {'orders': orders, 'categories': categories})

def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    categories = Category.objects.all()
    return render(request, 'store/order_detail.html', {'order': order, 'categories': categories})

def category_products(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = Product.objects.filter(category=category)
    categories = Category.objects.all()
    return render(request, 'store/category_products.html', {'products': products, 'category': category, 'categories': categories})
