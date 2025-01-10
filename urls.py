from django.contrib import admin
from django.urls import path
from bookstore import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('login',views.user_login),
    path('logout',views.user_logout),
    path('register',views.register),
    path('home',views.home),
    path('pdetails/<pid>',views.product_details),
    path('contact',views.contact),
    path('about',views.about),
    path('sort/<sv>',views.sort),
    path('range',views.range),
    path('catfilter/<cv>',views.catfilter),
    path('addtocart/<pid>',views.addtocart),
    path('remove/<cid>',views.remove),
    path('viewcart',views.viewcart),
    path('placeorder',views.placeorder),
    path('makepayment',views.makepayment),
    path('updateqty/<qv>/<cid>',views.updateqty),
    path('index',views.newhome),
    path('create',views.create),
    path('cart',views.cart),
    
]

if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
