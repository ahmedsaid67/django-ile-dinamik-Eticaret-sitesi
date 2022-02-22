from django.contrib import admin
from .models import Category,Product,Category1

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields={"slug":("title",)}
    list_display=('pk','title','gender','status','update_at',)
    list_filter=('status',)
    list_editable=('title','status',)

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields={"slug":("title",)}
    list_display=('pk','title','cover_image','price','stock','status','is_home',)
    list_filter=('status',)
    list_editable=('title','status','cover_image','is_home',)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Category1)