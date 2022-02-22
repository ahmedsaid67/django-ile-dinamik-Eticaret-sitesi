# Generated by Django 3.0 on 2022-02-12 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_product_is_home'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(default='', max_length=200)),
                ('status', models.CharField(choices=[('darft', 'taslak'), ('puplished', 'yayinlandi'), ('deleted', 'silindi')], default='draft', max_length=10)),
                ('gender', models.CharField(choices=[('man', 'erkek'), ('women', 'kadin'), ('unisex', 'unisex')], default='unisex', max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
