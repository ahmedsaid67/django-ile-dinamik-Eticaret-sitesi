from product.models import Category, Product
from django.shortcuts import render, get_object_or_404
from .models import STATUS, Carousel, Page, Slid

# Create your views here... context['category1'] = Category.objects.filter(status='puplished').order_by('title')

def index(request):
    context=dict()
    context['images'] = Slid.objects.filter(status='puplished').exclude(cover_image="").order_by("-id")
    context['products']=Product.objects.filter(status='puplished',is_home=True)
    return render(request,'home/index.html',context)

def page_show(request, page_slug):
    context=dict()
    context['page']=get_object_or_404(Page, slug=page_slug)
    return render(request,'page/page1.html',context)