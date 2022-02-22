from django.shortcuts import render, get_object_or_404
from .models import Category, Product, Category1

def category_show(request,category_slug):
    context=dict()
    #context['category1'] = Category.objects.filter(status='puplished').order_by('title')
    context['category']=get_object_or_404(Category,slug=category_slug)
    context['category5'] = Category1.objects.filter(status='puplished').order_by('title')
    context['items']=Product.objects.filter(
        category=context['category'],
        status="puplished",
        stock__gte=1,
    )
    return render( request,'product/category_show.html', context)
