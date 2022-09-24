from django.shortcuts import render,HttpResponse,redirect
from .form import ContactForm

# Create your views here.

def index(request):
    return render(request, 'pages/home.html', {'title': 'Home'})

def about(request):
    return render(request, 'pages/about.html', {'title': 'About'})

def product(request):
    return render(request, 'pages/products.html', {'title': 'Products'})

def contact(request):
    if request.method == "POST":
       form = ContactForm(request.POST)
       valid = form.is_valid()
       if valid:   
        form.save()
        return redirect('store:home')
    else:
        form = ContactForm()
        context = {
            'title': 'Contact',
            'form': form,
            }
        return render(request, 'pages/contact.html', context)