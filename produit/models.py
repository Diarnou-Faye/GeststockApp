from django.db import models


# Create your models here.
# Modèle des utilisateurs
class User(models.Model):
    username = models.CharField(
        max_length=20,
    )
    password = models.CharField(
        max_length=16,
    )


# Modéle des produits
class Product(models.Model):
    titre = models.CharField(max_length=70)
    description = models.CharField(max_length=1000)
    prix = models.CharField(max_length=20)
    nombre = models.IntegerField()
