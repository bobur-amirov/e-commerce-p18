from django.db.models import Prefetch, F, OuterRef, Subquery
from django.shortcuts import render, get_object_or_404

from product.models import Product, Images


def home(request):
    main_image_subquery = Images.objects.filter(
        product=OuterRef('pk'),
        is_main=True
    ).values('image')[:1]

    products = Product.objects.annotate(
        main_image=Subquery(main_image_subquery)
    ).values('title', 'price', 'main_image')

    context = {'products': products}
    return render(request, 'home.html', context)

def get_category(requets, pk):
    return render(requets, 'home.html')


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {"product": product}
    return render(request,'product/product_detail.html', context)