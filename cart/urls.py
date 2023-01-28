from django.urls import path
from . import views
app_name = 'cart'
urlpatterns = [
    path('', views.display_cart_details, name='cart_details'),
    path('added/<int:product_id>/', views.add_items_to_cart, name='add_to_cart'),
    path('removed/<int:product_id>/', views.remove_items_in_cart, name='remove_from_cart'),

]
