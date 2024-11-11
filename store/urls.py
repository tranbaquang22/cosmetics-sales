from django.contrib import admin
from django.urls import path
from store import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.product_list, name='home'),  # Trang chủ hiển thị danh sách sản phẩm
    path('products/', views.product_list, name='product_list'),  # Danh sách sản phẩm
    path('products/<int:product_id>/', views.product_detail, name='product_detail'),  # Chi tiết sản phẩm
    path('orders/', views.order_list, name='order_list'),  # Danh sách đơn hàng
    path('orders/<int:order_id>/', views.order_detail, name='order_detail'),  # Chi tiết đơn hàng
    path('category/<int:category_id>/', views.category_products, name='category_products'),  # Sản phẩm theo danh mục
    path('queries/', views.all_queries, name='all_queries'),  # Trang hiển thị các truy vấn thống kê
    path('stored_procedures/', views.stored_procedures, name='stored_procedures'),  # Trang hiển thị kết quả thủ tục

    # Đường dẫn thao tác với stored procedures
    path('add_product/', views.execute_add_product, name='execute_add_product'),  # Thêm sản phẩm qua stored procedure
    path('update_stock/', views.execute_update_stock, name='execute_update_stock'),  # Cập nhật tồn kho qua stored procedure
    path('delete_product/', views.execute_delete_product, name='execute_delete_product'),  # Xóa sản phẩm qua stored procedure
    path('add_order_detail/', views.execute_add_order_detail, name='execute_add_order_detail'),  # Thêm chi tiết đơn hàng qua stored procedure
]
