from product.models import Category
from page.models import Page

def nav_data(request):
    context= dict()
    context['category1'] = Category.objects.filter(status='puplished').order_by('title')
    context['pages'] = Page.objects.filter(status='puplished')
    return context
    