from django.contrib import admin
from .models import Page,Carousel,Slid
# Register your models here.

class PageAdmin(admin.ModelAdmin):
    prepopulated_fields={"slug":("title",)}
    list_display=('pk','title','status','update_at',)
    

admin.site.register(Page, PageAdmin)
admin.site.register(Slid)
