# Generated by Django 2.2.24 on 2021-09-17 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='slug',
            field=models.SlugField(default='', max_length=200),
        ),
    ]
