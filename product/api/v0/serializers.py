from rest_framework import serializers

from product.models import Product, Category, Comment, Images


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['pk', 'name', 'order']

    # Bu to_representation method bizga qo'shimcha field qo'shish imkonini beradi
    # shunda model ning fieldlaridan tashqari yana qo'shimcha field bulib client tamonga yuboriladi
    def to_representation(self, instance):
        data = super().to_representation(instance)
        # bu yerda get_FIEDNAME_display() choise field uchun ishlatiladi va
        # bizga choise ni labelni qaytaradi
        data['type_name'] = instance.get_type_display()
        return data


class ProductSerializer(serializers.ModelSerializer):
    main_image = serializers.CharField()

    class Meta:
        model = Product
        fields = ['pk', 'title', 'price', 'main_image']

    # def get_main_image(self, obj):
    #     main_image = obj.images_set.first()
    #     if main_image:
    #         return main_image.image.url
    #     return ""


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = ['pk', 'image']

class ProductDetailSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    images = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = ['pk', 'title', 'description',
                  'price', 'quantity', 'detail',
                  'images', 'category']

    def get_images(self, obj):
        images = Images.objects.filter(product=obj)
        serializer = ImageSerializer(images, many=True)
        return serializer.data


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['text', 'star', 'product']