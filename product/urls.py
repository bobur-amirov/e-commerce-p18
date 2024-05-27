from django.urls import path

from product import views

app_name = 'product'

urlpatterns = [
    path('', views.home, name='home'),
    path('store/', views.store, name='store'),
    path('category/<int:pk>', views.get_category, name='category'),
    path('product/<int:pk>', views.product_detail, name='detail')
]