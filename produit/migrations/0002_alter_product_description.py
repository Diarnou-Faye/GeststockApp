# Generated by Django 5.1 on 2024-08-24 19:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("produit", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="description",
            field=models.CharField(max_length=1000),
        ),
    ]
