from django.contrib.auth.decorators import login_required
from django.db.models import F, Sum
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db import IntegrityError

from order.models import Order, OrderItem
from product.models import Product


@login_required(login_url='/accounts/login/')
def cart(request):
    order = Order.objects.filter(customer=request.user,
                                 ordered=False).annotate(
        order_total_price=Sum('orderitem__total_price')
    ).first()

    context = {
        'order': order
    }
    return render(request, 'order/cart.html', context=context)


@login_required(login_url='/accounts/login/')
def add_order(request, pk):
    product = get_object_or_404(Product, pk=pk)
    order, order_created = Order.objects.get_or_create(
        customer=request.user,
        ordered=False
    )

    try:
        order_item, order_item_created = OrderItem.objects.get_or_create(
            product=product,
            customer=request.user,
            ordered=False,
            order=order

        )
    except IntegrityError:
        order_item, order_item_created = OrderItem.objects.get_or_create(
            product=product,
            customer=request.user,
            quantity=1,
            ordered=False,
            order=order

        )
    order_item.set_total_price()
    if not order_item_created:
        order_item.quantity += 1
        order_item.save()
        order_item.set_total_price()
        messages.info(request, f'{product.title} 1 ga oshirildi!')
        return redirect('order:cart')
    messages.info(request, 'savatchaga qo`shildi!')
    return redirect('order:cart')


@login_required(login_url='/accounts/login/')
def remove_order_item(request, pk):
    order_item = get_object_or_404(OrderItem, pk=pk)
    order_item.delete()
    return redirect('order:cart')





