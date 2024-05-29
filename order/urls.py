from django.urls import path

from . import views

app_name = 'order'

urlpatterns = [
    path('', views.cart, name='cart'),
    path('add/<int:pk>', views.add_order, name='add_order'),
    path('remove/<int:pk>', views.remove_order_item, name='remove_order_item')
]
