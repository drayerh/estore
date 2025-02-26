from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import Product, CartItem, Order
from .cart import CartManager
from .stripe_utils import create_stripe_checkout_session

def index(request):
    return render(request, 'shop/index.html')

def product_list(request):
    products = Product.objects.all()
    return render(request, 'shop/products.html', {'products': products})

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'shop/product_detail.html', {'product': product})

@login_required
def cart_detail(request):
    cart_manager = CartManager(request)
    cart_items = cart_manager.get_cart_items()
    total = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'shop/cart.html', {'cart_items': cart_items, 'total': total})

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_manager = CartManager(request)
    cart_manager.add_to_cart(product)
    return redirect('cart')

@login_required
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id)
    cart_item.delete()
    return redirect('cart')

@login_required
def checkout(request):
    cart_manager = CartManager(request)
    cart_items = cart_manager.get_cart_items()

    if not cart_items:
        return redirect('cart')

    success_url = request.build_absolute_uri(reverse('payment_success'))
    cancel_url = request.build_absolute_uri(reverse('cart'))

    checkout_session = create_stripe_checkout_session(
        cart_items,
        success_url,
        cancel_url
    )
    return redirect(checkout_session.url, code=303)

@login_required
def payment_success(request):
    return render(request, 'shop/success.html')