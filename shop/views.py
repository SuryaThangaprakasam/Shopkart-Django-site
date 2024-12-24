from django.shortcuts import render,redirect
from django.contrib import messages
from .models import *
from .forms import CustomerUserForm
from django.contrib.auth import authenticate,login,logout
from django.http import JsonResponse
import json

def index(request):
    trending_products = Product.objects.filter(trending=0).order_by('category')  #0-trending,1-no
    return render(request, 'index.html', {'trending_products':trending_products})

def register(request):
    form = CustomerUserForm()
    if request.method == 'POST':
        form = CustomerUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration success')
            return redirect('/login')
    return render(request, 'register.html', {'form':form})

def login_page(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            name = request.POST.get('username')
            pwd = request.POST.get('password')
            user = authenticate(request, username=name, password=pwd)
            if user is not None:
                login(request, user)
                messages.success(request, 'Logged in Successfully')
                return redirect('/')
            else:
                messages.error(request, 'Invalid credentials')
    return render(request, 'login.html')

def logout_page(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, 'Logged out Successfully')
    return redirect('/')

def collections(request):
    category = Category.objects.filter(status=0)
    return render(request, 'collections.html', {'category':category})

def collectionsview(request, name):
    if (Category.objects.filter(name=name, status=0)):
        products = Product.objects.filter(category__name=name)
        return render(request, 'product_index.html', {'products':products,'cat_name':name})
    else:
        messages.warning(request, "No such category found")
        return redirect('/collections')

def productdetails(request, cname, pname):
    if (Category.objects.filter(name=cname, status=0) and Product.objects.filter(name=pname, status=0).first()):
        product = Product.objects.filter(name=pname, status=0).first()
        return render(request, 'product_detail.html', {'product':product})
    else:
        messages.warning(request, "No such data")
        return redirect('/collections')
    
def add_to_cart(request):
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':     #caps wrong check, if any goes wrong
        if request.user.is_authenticated:
            data = json.loads(request.body)
            print(request)
            print(data)
            product_qty = data['product_qty']
            product_id = data['pid']
            product_obj = Product.objects.get(id=product_id)
            if product_obj:
                if Cart.objects.filter(user=request.user, product_id=product_id):
                    return JsonResponse({'status':f'"{product_obj}" Already in the cart'}, status=200)
                else:
                    if product_obj.quantity >= product_qty:
                        Cart.objects.create(user=request.user, product=product_obj, product_qty=product_qty)
                        return JsonResponse({'status':f'"{product_obj}" is now added to cart'}, status=200)
                    else:
                        return JsonResponse({'status':'Product Stock not available'}, status=200)
            else:
                return JsonResponse({'status':'Product not available'}, status=200)
        else:
            return JsonResponse({'status':'Unauthourised Access, Login to use Cart'}, status=200)

def cart(request):
    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user)
        return render(request, 'cart.html', {'cart':cart})
    else:
        messages.warning(request, "Login to access your Cart")
        return redirect('/login')

def remove_cart(request,id):
    if request.user.is_authenticated:
        cart_item = Cart.objects.get(id=id)
        messages.warning(request, f"'{cart_item.product.name}' removed from your cart")
        cart_item.delete()
        return redirect('/cart')

def add_to_wishlist(request):
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        if request.user.is_authenticated:
            data = json.loads(request.body)
            print(request)
            print(data)
            product_id = data['pid']
            product_obj = Product.objects.get(id=product_id)
            if product_obj:
                if Wishlist.objects.filter(user=request.user, product_id=product_id):
                    return JsonResponse({'status':f'"{product_obj}" Already in the Wishlist'}, status=200)
                else:
                    Wishlist.objects.create(user=request.user, product=product_obj)
                    return JsonResponse({'status':f'"{product_obj}" is now added to Wishlist'}, status=200)
            else:
                return JsonResponse({'status':'Product not available'}, status=200)
        else:
            return JsonResponse({'status':'Unauthourised Access, Login to use Wishlist'}, status=200)

def wishlist(request):
    if request.user.is_authenticated:
        wishlist = Wishlist.objects.filter(user=request.user)
        return render(request, 'wishlist.html', {'wishlist':wishlist})
    else:
        messages.warning(request, "Login to access your Wishlist")
        return redirect('/login')

def remove_wishlist(request,id):
    if request.user.is_authenticated:
        wishlist_item = Wishlist.objects.get(id=id)
        messages.warning(request, f"'{wishlist_item.product.name}' removed from your Wishlist")
        wishlist_item.delete()
        return redirect('/wishlist')