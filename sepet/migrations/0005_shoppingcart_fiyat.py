# Generated by Django 2.2.24 on 2021-10-19 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sepet', '0004_auto_20211010_0058'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoppingcart',
            name='fiyat',
            field=models.FloatField(default=0),
        ),
    ]
