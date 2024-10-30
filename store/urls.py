from django.contrib import admin
from django.urls import path, include
from store import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.product_list, name='home'),
    path('products/', views.product_list, name='product_list'),
    path('products/<int:product_id>/', views.product_detail, name='product_detail'),
    path('orders/', views.order_list, name='order_list'),
    path('orders/<int:order_id>/', views.order_detail, name='order_detail'),
    path('category/<int:category_id>/', views.category_products, name='category_products'),  # Trang sản phẩm theo danh mục
    path('queries/', views.all_queries, name='all_queries'),  # Trang hiển thị truy vấn
    path('stored_procedures/', views.stored_procedures, name='stored_procedures'),  # Trang hiển thị kết quả thủ tục riêng
    path('add_product/', views.execute_add_product, name='execute_add_product'),
    path('update_stock/', views.execute_update_stock, name='execute_update_stock'),
    path('delete_product/', views.execute_delete_product, name='execute_delete_product'),
    path('add_order_detail/', views.execute_add_order_detail, name='execute_add_order_detail'),

]

