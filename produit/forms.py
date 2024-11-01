from django.core import validators
from django import forms
from .models import Product, User


# Formulaire des utilisateurs
class UserRegistration(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "password"]
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "password": forms.TextInput(attrs={"class": "form-control"}),
        }


# Formulaire des Produits
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
