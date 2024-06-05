from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .serializers import (CategorySerializer,
                          ProductSerializer,
                          ProductDetailSerializer,
                          CommentCreateSerializer
                          )
from product.models import Category, Product, Comment


class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    # bu yerda get_querset nima ekanligi tushuntirildi
    # def get_queryset(self):
    #     qs = super().get_queryset()
    #     ids = [1, 3]
    #     qs = qs.filter(id__in=ids)
    #     return qs


class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductByCategoryListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        pk = self.kwargs.get('pk')
        qs = qs.filter(category=pk)
        return qs


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.select_related('category'
                                              ).prefetch_related('images_set').all()
    serializer_class = ProductDetailSerializer


class CommentCreateAPIView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentCreateSerializer
    permission_classes = (IsAuthenticated, )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
