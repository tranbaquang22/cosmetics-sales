from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'category', 'brand', 'price', 'stock', 'skin_type', 'description', 'image']  # Cập nhật các trường
