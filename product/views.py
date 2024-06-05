from django.db.models import Prefetch, F, OuterRef, Subquery, Avg
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.urls import reverse

from product.models import Product, Images, Comment, Category
from product.filters import ProductFilter


def home(request):
    main_image_subquery = Images.objects.filter(
        product=OuterRef('pk'),
        is_main=True
    ).values('image')[:1]

    products = Product.objects.annotate(
        main_image=Subquery(main_image_subquery)
    ).values('pk', 'title', 'price', 'main_image')[:8]

    context = {'products': products}
    return render(request, 'home.html', context)


def store(request):
    main_image_subquery = Images.objects.filter(
        product=OuterRef('pk'),
        # is_main=True
    ).values('image')[:1]

    price_gte = request.GET.get('price__gte')
    price_lte = request.GET.get('price__lte')
    if price_lte and price_gte:
        products = Product.objects.filter(price__gte=price_gte, price__lte=price_lte)
    elif price_gte and not price_lte:
        products = Product.objects.filter(price__gte=price_gte)
    else:
        products = Product.objects.all()

    products = products.annotate(
        main_image=Subquery(main_image_subquery)
    ).values('pk', 'title', 'price', 'main_image')

    products = Paginator(products, 3)
    page = request.GET.get('page')
    try:
        products = products.page(page)
    except (PageNotAnInteger, EmptyPage):
        products = products.page(1)

    # products = ProductFilter(request.GET, queryset=page_products.object_list)
    context = {'products': products}
    return render(request, 'product/store.html', context)

def get_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    main_image_subquery = Images.objects.filter(
        product=OuterRef('pk'),
        # is_main=True
    ).values('image')[:1]

    products = Product.objects.filter(category=category).annotate(
        main_image=Subquery(main_image_subquery)
    ).values('pk', 'title', 'price', 'main_image')

    products = Paginator(products, 3)
    page = request.GET.get('page')
    try:
        products = products.page(page)
    except (PageNotAnInteger, EmptyPage):
        products = products.page(1)

    context = {'products': products, "category": category}
    return render(request, 'product/store.html', context)


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        text = request.POST.get('text')
        star = request.POST.get('star')
        if request.user.is_authenticated:
            comment = Comment.objects.create(
                product=product,
                owner=request.user,
                text=text,
                star=star if star else 0
            )
            return redirect(reverse('product:detail', kwargs={"pk": product.pk}))
    avg_rating = product.comment_set.filter(star__gt=0).aggregate(Avg('star'))['star__avg']
    context = {"product": product, "star_avg": avg_rating}
    return render(request, 'product/product_detail.html', context)
