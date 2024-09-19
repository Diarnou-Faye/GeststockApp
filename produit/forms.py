from django.core import validators
from django import forms
from .models import Product


class ProductRegistration(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["titre", "description", "prix", "nombre"]
        widgets = {
            "titre": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control"}),
            "prix": forms.TextInput(attrs={"class": "form-control"}),
            "nombre": forms.NumberInput(attrs={"class": "form-control"}),
        }
