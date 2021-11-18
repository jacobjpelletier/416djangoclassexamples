from django import forms  # (1)
from .models import Product  # (1)

'''
first used to create product in view.py

1. first import django forms and Product model
2. extend django form to create a new product form which connects to model Product
'''


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product  # (2)
        fields = '__all__'  # use all table columns (fields)
