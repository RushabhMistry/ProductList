from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'quantity', 'price']

    def clean_quantity(self):
        quantity = self.cleaned_data.get('quantity')
        if quantity <= 0:
            raise forms.ValidationError("Quantity must be greater than zero.")
        return quantity

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price <= 0:
            raise forms.ValidationError("Price must be greater than zero.")
        return price

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if name:
            # Check if a product with the same name already exists
            existing_product = Product.objects.filter(name=name).exists()
            if existing_product:
                raise forms.ValidationError("A product with this name already exists.")
        return name