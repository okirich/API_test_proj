from rest_framework import serializers
from .models import Address,Shop

class AddressSerializer(serializers.ModelSerializer):
    shops = serializers.PrimaryKeyRelatedField(
        many=True,
        read_only=True
        )
    class Meta:
        model = Address
        fields = ['id','street','building','shops']

class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = '__all__'