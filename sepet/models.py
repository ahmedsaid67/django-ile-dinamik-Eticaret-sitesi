from django.db import models
from django.db.models.deletion import CASCADE
from product.models import Product
from django.contrib.auth.models import User

STATUS=[('waiting','bekleniyor'),
('buyed','satinalindi'),
('deleted','silindi'),
]

class ShopingCartItem(models.Model):
    user=models.ForeignKey(
        User, blank=True, null= True, on_delete= CASCADE
    )
    product=models.ForeignKey(Product, on_delete=CASCADE)
    price=models.FloatField(default=0)
    is_deleted=models.BooleanField(default=False)
    createt_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.title+", Fiyat:"+str(self.price)

    
class ShoppingCart(models.Model):
    user=models.ForeignKey(
        User, blank=True, null= True, on_delete= CASCADE
    )
    product=models.ManyToManyField(Product)
    items=models.ManyToManyField(ShopingCartItem,null=True, blank=True)
    total_price=models.FloatField(default=0)
    session_key=models.CharField(max_length=32,blank=True,null=True)
    status=models.CharField(
        default="waiting",
        choices=STATUS,
        max_length=10,
    )
    createt_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "PK: "+str(self.pk)+"  Total: "+str(self.total_price)+"  Status: "+self.status


class Product:
    pass