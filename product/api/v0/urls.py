from django.urls import path

from . import views


urlpatterns = [
    path('categories/', views.CategoryListAPIView.as_view(), name='category_list'),
    path('products/', views.ProductListAPIView.as_view(), name='product_list'),
    path('category/<int:pk>', views.ProductByCategoryListAPIView.as_view(), name='product_category_list'),
    path('product/<int:pk>', views.ProductDetailAPIView.as_view(), name='product_detail'),
    path('comment-create/', views.CommentCreateAPIView.as_view(), name='comment_create'),
]