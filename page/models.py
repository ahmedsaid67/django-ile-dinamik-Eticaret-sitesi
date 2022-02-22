from django.db import models

# Create your models here.

STATUS=[('darft','taslak'),
('puplished','yayinlandi'),
('deleted','silindi'),
]

class Page(models.Model):
    title=models.CharField(max_length=200)
    slug=models.SlugField(max_length=200, default="")
    content=models.TextField()
    cover_image=models.ImageField(upload_to='page',null=True,blank=True,)
    status=models.CharField(
        default='draft',
        choices=STATUS,
        max_length=10,
    )
    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now_add=True)
 

class Carousel(models.Model):
    title=models.CharField(max_length=200)
    cover_image=models.ImageField(upload_to='carousel',null=True,blank=True,)
    status=models.CharField(
        default='draft',
        choices=STATUS,
        max_length=10,
    )
    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now_add=True)
 
class Slid(models.Model):
    title=models.CharField(max_length=200)
    cover_image=models.ImageField(upload_to='carousel',null=True,blank=True,)
    status=models.CharField(
        default='draft',
        choices=STATUS,
        max_length=10,
    )
    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now_add=True)

