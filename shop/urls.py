from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('register',views.register),
    path('login',views.login_page), #we have a built-in func named 'login' so we used 'login_page'
    path('logout',views.logout_page),
    path('collections',views.collections),
    path('collections/<str:name>',views.collectionsview),
    path('collections/<str:cname>/<str:pname>',views.productdetails),

    path('addtocart', views.add_to_cart),
    path('cart',views.cart),
    path('cart/remove/<int:id>',views.remove_cart),

    path('addtowishlist',views.add_to_wishlist),
    path('wishlist',views.wishlist),
    path('wishlist/remove/<int:id>',views.remove_wishlist)
]