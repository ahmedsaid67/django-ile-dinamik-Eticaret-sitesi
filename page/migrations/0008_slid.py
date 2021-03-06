# Generated by Django 3.0 on 2022-02-12 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0007_auto_20210920_1711'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('cover_image', models.ImageField(blank=True, null=True, upload_to='carousel')),
                ('status', models.CharField(choices=[('darft', 'taslak'), ('puplished', 'yayinlandi'), ('deleted', 'silindi')], default='draft', max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
