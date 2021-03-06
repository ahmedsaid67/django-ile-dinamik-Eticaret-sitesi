# Generated by Django 2.2.24 on 2021-09-22 15:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(default='', max_length=200)),
                ('status', models.CharField(choices=[('darft', 'taslak'), ('puplished', 'yayinlandi'), ('deleted', 'silindi')], default='draft', max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(default='', max_length=200)),
                ('content', models.TextField()),
                ('cover_image', models.ImageField(blank=True, null=True, upload_to='page')),
                ('price', models.FloatField()),
                ('stock', models.PositiveSmallIntegerField(default=0)),
                ('status', models.CharField(choices=[('darft', 'taslak'), ('puplished', 'yayinlandi'), ('deleted', 'silindi')], default='draft', max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Category')),
            ],
        ),
    ]
