# Generated by Django 2.2.24 on 2021-09-18 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0005_corousel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='corousel',
            name='cover_image',
            field=models.ImageField(blank=True, null=True, upload_to='carousel'),
        ),
    ]