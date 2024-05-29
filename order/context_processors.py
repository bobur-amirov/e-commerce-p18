from .models import OrderItem


def order_count(request):
    if request.user.is_authenticated:
        count = OrderItem.objects.filter(customer=request.user, ordered=False).count()
    else:
        count = 0
    return {"count": count}