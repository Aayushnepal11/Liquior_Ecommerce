from django.shortcuts import render, get_object_or_404, redirect
from . forms import ADDtoCartForm
from shop.models import Product
from .cart import Cart
from django.views.decorators.http import require_POST


# Create your views here.
@require_POST
def add_items_to_cart(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = ADDtoCartForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add_to_cart(product=product, quantity=cd['quantity'], override_quantity=cd['override'])
    return redirect('cart:cart_details')


@require_POST
def remove_items_in_cart(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove_from_cart(product)
    return redirect('cart:cart_details')


def display_cart_details(request):
    cart = Cart(request)
    for items in cart:
        items['update_quantity_form'] = ADDtoCartForm(initial={
            'quantity': items['quantity'],
            'override': True
        })
    return render(request, 'cart/details.html', {'cart': cart})
