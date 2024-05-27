from django.db.models import Prefetch, F, OuterRef, Subquery, Avg
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from product.models import Product, Images, Comment


def home(request):
    main_image_subquery = Images.objects.filter(
        product=OuterRef('pk'),
        is_main=True
    ).values('image')[:1]

    products = Product.objects.annotate(
        main_image=Subquery(main_image_subquery)
    ).values('pk', 'title', 'price', 'main_image')

    context = {'products': products}
    return render(request, 'home.html', context)


def get_category(requets, pk):
    return render(requets, 'home.html')


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        text = request.POST.get('text')
        star = request.POST.get('star')
        print(star)
        if request.user.is_authenticated:
            comment = Comment.objects.create(
                product=product,
                owner=request.user,
                text=text,
                star=star if star else 0
            )
            return redirect(reverse('product:detail', kwargs={"pk": product.pk}))
    avg_rating = product.comment_set.filter(star__gt=0).aggregate(Avg('star'))['star__avg']
    print(avg_rating, '--')
    context = {"product": product, "star_avg": avg_rating}
    return render(request, 'product/product_detail.html', context)
