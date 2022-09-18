from rest_framework import serializers

from .models import ProductApi, ProductDetails

class ProductApiSerialzer(serializers.HyperlinkedModelSerializer):
    product_name = serializers.RelatedField(source='product', read_only=True)
    class Meta:
        model = ProductApi
        fields = ('title', 'description', 'price' , "product_name" )