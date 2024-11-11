from django.contrib import admin
from .models import Category, Brand, Product, Order, OrderDetail
from django.utils import timezone

# Inline cho OrderDetail để hiển thị chi tiết đơn hàng trong Order
class OrderDetailInline(admin.TabularInline):
    model = OrderDetail
    extra = 1  # Số hàng trống để thêm chi tiết mới nếu cần
    fields = ('product', 'quantity', 'price')

# Đăng ký model Category (Danh mục sản phẩm)
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')  # Hiển thị các trường trong danh sách
    search_fields = ('name',)  # Cho phép tìm kiếm theo tên

# Đăng ký model Brand (Thương hiệu mỹ phẩm)
@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'origin_country')  # Hiển thị tên và quốc gia xuất xứ của thương hiệu
    search_fields = ('name',)  # Cho phép tìm kiếm theo tên thương hiệu

# Đăng ký model Product (Sản phẩm mỹ phẩm)
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'brand', 'price', 'stock', 'skin_type')  # Hiển thị các trường quan trọng
    list_filter = ('category', 'brand', 'skin_type')  # Thêm bộ lọc theo danh mục, thương hiệu, và loại da
    search_fields = ('name',)  # Cho phép tìm kiếm theo tên sản phẩm
    fields = ('name', 'category', 'brand', 'price', 'stock', 'skin_type', 'description', 'image')

# Đăng ký model Order (Đơn hàng)
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer_name', 'date_ordered', 'status')  # Hiển thị các trường trong danh sách
    list_filter = ('status',)  # Thêm bộ lọc theo trạng thái đơn hàng
    search_fields = ('customer_name',)  # Cho phép tìm kiếm theo tên khách hàng
    inlines = [OrderDetailInline]  # Inline để hiển thị chi tiết đơn hàng
    fields = ('customer_name', 'customer_address', 'customer_phone', 'date_ordered', 'status')
    
    # Đặt mặc định date_ordered là ngày hiện tại khi thêm mới đơn hàng
    def get_changeform_initial_data(self, request):
        return {'date_ordered': timezone.now()}

# Đăng ký model OrderDetail (Chi tiết đơn hàng)
@admin.register(OrderDetail)
class OrderDetailAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'product', 'quantity', 'price')  # Hiển thị các trường trong danh sách
