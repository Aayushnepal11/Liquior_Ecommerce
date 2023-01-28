from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .form import ContactForm

from django.contrib import messages
from .models import Product, Category

from cart.forms import ADDtoCartForm


# Create your views here.

def index(request):
    content = {
        'title': 'Home',

    }
    return render(request, 'pages/home.html', content)


def about(request):
    return render(request, 'pages/about.html', {'title': 'About'})


def product(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    context = {
        'title': 'Products',
        'products': products,
        'categories': categories
    }
    return render(request, 'pages/products.html', context)


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    context = {
        'category': category,
        'categories': categories,
        'products': products,

    }
    return render(request, 'pages/products.html', context)


def product_detail(request, id, slug):
    products = get_object_or_404(Product, id=id, slug=slug, available=True)
    add_to_cart_form = ADDtoCartForm()
    context = {
        'products': products,
        'cartForm': add_to_cart_form
    }

    return render(request, 'pages/product_details.html', context)


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'FeedBack Sent Sucessfully')
            return redirect('store:contact')
    else:
        form = ContactForm()
        context = {
            'title': 'Contact',
            'form': form,
        }
        return render(request, 'pages/contact.html', context)
