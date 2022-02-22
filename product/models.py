from django.db import models

# Create your models here.

STATUS=[('darft','taslak'),
('puplished','yayinlandi'),
('deleted','silindi'),
]

GENDER=[('man','erkek'),
('women','kadin'),
('unisex','unisex'),
]

class Category(models.Model):
    title=models.CharField(max_length=200)
    slug=models.SlugField(max_length=200, default="")
    status=models.CharField(
        default='draft',
        choices=STATUS,
        max_length=10,
    )
    gender=models.CharField(
        default='unisex',
        choices=GENDER,
        max_length=10)
    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.gender+"-"+self.title

class Category1(models.Model):
    title=models.CharField(max_length=200)
    slug=models.SlugField(max_length=200, default="")
    status=models.CharField(
        default='draft',
        choices=STATUS,
        max_length=10,
    )
    gender=models.CharField(
        default='unisex',
        choices=GENDER,
        max_length=10)
    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.gender+"-"+self.title

class Product(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    slug=models.SlugField(max_length=200, default="")
    content=models.TextField()
    cover_image=models.ImageField(upload_to='page',null=True,blank=True,)
    price=models.FloatField()
    is_home=models.BooleanField(default=False)
    stock=models.PositiveSmallIntegerField(default=0)
    status=models.CharField(
        default='draft',
        choices=STATUS,
        max_length=10,
    )
    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
 