# Generated by Django 2.2.24 on 2021-10-19 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_product_is_home'),
        ('sepet', '0007_auto_20211019_1903'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoppingcart',
            name='product',
            field=models.ManyToManyField(to='product.Product'),
        ),
    ]
