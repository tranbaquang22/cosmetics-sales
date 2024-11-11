# store/models.py
from django.db import models
from django.utils import timezone

# Bảng danh mục sản phẩm (Category Table)
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

# Bảng thương hiệu mỹ phẩm (Brand Table)
class Brand(models.Model):
    name = models.CharField(max_length=100)
    origin_country = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

# Bảng sản phẩm mỹ phẩm (Product Table)
class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    skin_type = models.CharField(max_length=50, choices=[
        ('All', 'All'), 
        ('Dry', 'Dry'), 
        ('Oily', 'Oily'), 
        ('Sensitive', 'Sensitive'), 
        ('Normal', 'Normal')
    ], default='All')
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)

    def __str__(self):
        return self.name

# Bảng đơn hàng (Order Table)
class Order(models.Model):
    customer_name = models.CharField(max_length=100)
    customer_address = models.TextField()
    customer_phone = models.CharField(max_length=15)
    date_ordered = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=20, choices=[
        ('Pending', 'Pending'), 
        ('Shipped', 'Shipped'), 
        ('Delivered', 'Delivered'), 
        ('Cancelled', 'Cancelled'), 
    ], default='Pending')

    def __str__(self):
        return f"Order {self.id}"

# Bảng chi tiết đơn hàng (Order Detail Table)
class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.product.name} ({self.quantity})"
