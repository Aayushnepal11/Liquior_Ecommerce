from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import login
from django.contrib.auth.forms  import UserCreationForm
# from . form import UserCreationForm
# from . models import CustomerUsers
# Create your views here.
def register(request):
    """ Creating the new user to be able to regsiter """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            redirect('store:index')
    else:
        form = UserCreationForm()
        context = {
            'title': 'Register',
            'form': form
            }
        return render(request, 'registration/register.html', context)
    