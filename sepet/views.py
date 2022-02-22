from django.shortcuts import render,redirect
from .models import ShopingCartItem,ShoppingCart
from .models import Product
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import UserRegisterForm
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
import hashlib
import base64
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import urllib.parse, requests
from product.models import Product




def user(request,user_pk):
    if request.user.is_authenticated:
        user=request.user
        shopping_cart=ShoppingCart.objects.filter(user=user, status="waiting")
        if shopping_cart.count()>0:
            shopping_cart=shopping_cart.last()
        else:
            shopping_cart=ShoppingCart.objects.create(user=user)

        shopping_cart.session_key=request.session.session_key
        urun=Product.objects.get(pk=user_pk)
        uruns=urun.price
        isim=urun.title
        shopping_cart_item=ShopingCartItem.objects.create(user=user,product=urun,price=uruns)
        shopping_cart.total_price+=uruns
        shopping_cart.items.set=isim
        shopping_cart.save()
        return redirect("/")
    return redirect("/login/")


def user_register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user=authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'Account created ')
            return redirect("/")
    form = UserRegisterForm()
    return render(request, 'sepet/register.html',{'form':form})



def user_sepet(request):
    context=dict()
    if request.user.is_authenticated:
        user=request.user
        shopping_cart=ShoppingCart.objects.filter(user=user, status="waiting")

        if shopping_cart.count()>0:
            context['carts']=shopping_cart
            shopping_cart_item=ShopingCartItem.objects.filter(user=user)
            context['items']=shopping_cart_item
            return render(request, 'sepet/sepet.html',context)
    return redirect("/")



def user_logout(request):
    return render(request, 'sepet/login.html')


