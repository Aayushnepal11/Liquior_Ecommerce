from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('products/', views.product, name='product'),
]
