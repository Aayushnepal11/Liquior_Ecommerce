from django.shortcuts import render, HttpResponse, redirect
from .form import ContactForm

from django.contrib import messages

from .models import FeaturedProducts


# Create your views here.

def index(request):
    featured = FeaturedProducts.objects.all()
    content = {
        'title': 'Home',
        'featured': featured,
    }
    return render(request, 'pages/home.html', content)


def about(request):
    return render(request, 'pages/about.html', {'title': 'About'})


def product(request):
    return render(request, 'pages/products.html', {'title': 'Products'})


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
