from rest_framework import serializers

from products.models import Product



class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Product

    def validate_name(self, value):
        if not value.isalnum():
            raise serializers.ValidationError("Name should be alphanumeric")
        
        if Product.objects.filter(name=value, is_deleted=False).exists():
            raise serializers.ValidationError("Product with this name already exists")
        return value