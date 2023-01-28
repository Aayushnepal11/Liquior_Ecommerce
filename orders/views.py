from django.shortcuts import render
from cart.cart import Cart
from .models import OrderedItem
from .forms import OrderForm


# Create your views here.

def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            for items in cart:
                OrderedItem.objects.create(order=order, product=items['product'],
                                           price=items['price'],
                                           quantity=items['quantity'])
            cart.clear()
            return render(request, 'orders/created.html', {'order': order})
    else:
        form = OrderForm()

    return render(request, 'orders/create.html', {'form': form,
                                                  'cart': cart})



