from django.db import connection
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Order, Category, Brand, OrderDetail
from django.db.models import Avg, Max, Min, Count
from django.contrib import messages

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

# View để hiển thị tất cả các truy vấn
def all_queries(request):
    queries = {
        'total_products': Product.objects.count(),
        'total_orders': Order.objects.count(),
        'average_price': Product.objects.aggregate(Avg('price'))['price__avg'],
        'max_price': Product.objects.aggregate(Max('price'))['price__max'],
        'min_price': Product.objects.aggregate(Min('price'))['price__min'],
        'category_count': Category.objects.count(),
        'products_per_category': Product.objects.values('category__name').annotate(total=Count('id')).order_by('-total'),
        'orders_per_status': Order.objects.values('status').annotate(total=Count('id')).order_by('-total'),
        'most_expensive_product': Product.objects.order_by('-price').first(),
        'least_stocked_product': Product.objects.order_by('stock').first(),
    }

    categories = Category.objects.all()
    return render(request, 'store/all_queries.html', {'queries': queries, 'categories': categories})

def call_stored_procedure(procedure_name, params):
    """Utility function to call an Oracle stored procedure using Django's managed connection."""
    with connection.cursor() as cursor:
        try:
            cursor.callproc(procedure_name, params)
            connection.commit()
        except Exception as e:
            connection.rollback()
            raise e

def execute_add_product(request):
    if request.method == 'POST':
        category_id = int(request.POST.get('category_id', 1))
        brand_id = int(request.POST.get('brand_id', 1))

        # Kiểm tra sự tồn tại của category_id và brand_id
        if not Category.objects.filter(id=category_id).exists():
            messages.error(request, 'Lỗi: Danh mục không tồn tại.')
            return redirect('stored_procedures')

        if not Brand.objects.filter(id=brand_id).exists():
            messages.error(request, 'Lỗi: Thương hiệu không tồn tại.')
            return redirect('stored_procedures')

        params = [
            request.POST.get('name', 'Sample Product'),
            category_id,
            brand_id,
            float(request.POST.get('price', 100.0)),
            int(request.POST.get('stock', 50)),
            request.POST.get('skin_type', 'All'),
            request.POST.get('description', 'Sample Description'),
            request.POST.get('image', 'default.jpg')
        ]

        try:
            call_stored_procedure('ADD_PRODUCT_PROC', params)
            messages.success(request, 'Thêm sản phẩm thành công!')
        except Exception as e:
            if 'ORA-02291' in str(e):
                messages.error(request, 'Lỗi: Không tìm thấy khóa ngoại hợp lệ (Danh mục hoặc Thương hiệu).')
            else:
                messages.error(request, f'Lỗi: {str(e)}')
    return redirect('stored_procedures')

def execute_delete_product(request):
    if request.method == 'POST':
        product_id = int(request.POST.get('product_id', 1))

        # Kiểm tra nếu sản phẩm có ràng buộc với OrderDetail
        if OrderDetail.objects.filter(product_id=product_id).exists():
            messages.error(request, 'Lỗi: Không thể xóa sản phẩm vì có bản ghi liên quan trong OrderDetail.')
            return redirect('stored_procedures')

        params = [product_id]

        try:
            call_stored_procedure('DELETE_PRODUCT_PROC', params)
            messages.success(request, 'Xóa sản phẩm thành công!')
        except Exception as e:
            if 'ORA-02292' in str(e):
                messages.error(request, 'Lỗi: Không thể xóa vì ràng buộc khóa ngoại (bản ghi con tồn tại).')
            else:
                messages.error(request, f'Lỗi: {str(e)}')
    return redirect('stored_procedures')

def execute_update_stock(request):
    if request.method == 'POST':
        params = [
            int(request.POST.get('product_id', 1)),
            int(request.POST.get('new_stock', 100))
        ]
        try:
            call_stored_procedure('UPDATE_PRODUCT_STOCK_PROC', params)
            messages.success(request, 'Cập nhật tồn kho thành công!')
        except Exception as e:
            messages.error(request, f'Lỗi: {str(e)}')
    return redirect('stored_procedures')

def execute_add_order_detail(request):
    if request.method == 'POST':
        params = [
            int(request.POST.get('order_id', 1)),
            int(request.POST.get('product_id', 1)),
            int(request.POST.get('quantity', 1)),
            float(request.POST.get('price', 100.0))
        ]
        try:
            call_stored_procedure('ADD_ORDER_DETAIL_PROC', params)
            messages.success(request, 'Thêm chi tiết đơn hàng thành công!')
        except Exception as e:
            messages.error(request, f'Lỗi: {str(e)}')
    return redirect('stored_procedures')

def stored_procedures(request):
    # Lấy danh sách các danh mục, thương hiệu, sản phẩm, và đơn hàng
    categories = Category.objects.all()
    brands = Brand.objects.all()
    products = Product.objects.all()
    orders = Order.objects.all()
    return render(request, 'store/stored_procedures.html', {
        'categories': categories,
        'brands': brands,
        'products': products,
        'orders': orders,
    })
