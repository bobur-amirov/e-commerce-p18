from django.db.models import Sum
from rest_framework import serializers

from order.models import Order, OrderItem
from product.models import Images


class OrderItemSerializer(serializers.ModelSerializer):
    product_title = serializers.CharField(source='product.title')
    product_price = serializers.IntegerField(source='product.price')
    main_image = serializers.SerializerMethodField()

    class Meta:
        model = OrderItem
        fields = ['product_title', 'product_price', 'main_image',
                  'quantity', 'total_price']

    def get_main_image(self, obj):
        main_image = Images.objects.filter(product=obj.product).first()
        if main_image:
            return main_image.image.url
        return ""

class OrderSerializer(serializers.ModelSerializer):
    orderitems = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ['pk', 'total_price', 'orderitems']

    def get_orderitems(self, obj):
        orderitems = OrderItem.objects.filter(order=obj)
        serializer = OrderItemSerializer(orderitems, many=True)
        return serializer.data
