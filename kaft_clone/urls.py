from re import template
from unicodedata import name
from django.contrib import admin
from django.urls import path, include
from page.views import page_show
from page.views import index
from product.views import category_show
from django.conf import settings
from django.conf.urls.static import static
from sepet.views import user,user_register,user_sepet,user_logout
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import logout_then_login
urlpatterns = [
    path('',index,name='index'),
    path('login/', auth_views.LoginView.as_view(template_name='sepet/giris1.html'), name='login'),
    path('logout', user_logout, name='logout'),
    path('logout1',auth_views.LogoutView.as_view() , name='logout1'),
    path('user/<int:user_pk>/',user, name='users'),
    path('register',user_register, name='register'),
    path('sepet',user_sepet, name='sepet'),
    path('<slug:category_slug>',category_show,name='category_show'),
    path('page/<slug:page_slug>/',page_show, name='page_show'),
    path('admin/', admin.site.urls),
]

urlpatterns += static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)
