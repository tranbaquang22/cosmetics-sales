from django.contrib import admin
from .models import Category, Supplier, Product, Order, OrderDetail
from django.utils import timezone

# Inline cho OrderDetail để hiển thị chi tiết đơn hàng trong Order
class OrderDetailInline(admin.TabularInline):
    model = OrderDetail
    extra = 1  # Số hàng trống để thêm chi tiết mới nếu cần
    fields = ('product', 'quantity', 'price')
# Đăng ký model Category
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')  # Hiển thị các trường trong danh sách
    search_fields = ('name',)  # Cho phép tìm kiếm theo tên

# Đăng ký model Supplier
@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'email')
    search_fields = ('name',)

# Đăng ký model Product
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'price', 'stock','image')
    list_filter = ('category',)  # Thêm bộ lọc theo danh mục
    search_fields = ('name',)  # Cho phép tìm kiếm theo tên
    fields = ('name', 'category', 'supplier', 'price', 'stock', 'description', 'image')
# Đăng ký model Order
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer_name', 'date_ordered', 'status')
    list_filter = ('status',)  # Thêm bộ lọc theo trạng thái
    search_fields = ('customer_name',)
    inlines = [OrderDetailInline]
    # Thêm date_ordered vào fields để có thể chỉnh sửa trong admin
    fields = ('customer_name', 'customer_address', 'customer_phone', 'date_ordered', 'status')
    # Đặt mặc định date_ordered là ngày hiện tại khi thêm mới
    def get_changeform_initial_data(self, request):
        return {'date_ordered': timezone.now()}
# Đăng ký model OrderDetail
@admin.register(OrderDetail)
class OrderDetailAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'product', 'quantity', 'price')
