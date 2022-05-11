from rest_framework import serializers
from .models import Address,Shop

class AddressSerializer(serializers.ModelSerializer):
    shops = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Shop.objects.all(),
        )
    url = serializers.HyperlinkedIdentityField('addr-detail')
    class Meta:
        model = Address
        fields = ['id','street','building','shops','url']

class ShopSerializer(serializers.ModelSerializer):
    address = serializers.PrimaryKeyRelatedField(
        many=False,
        queryset=Address.objects.all(),
    )
    url = serializers.HyperlinkedIdentityField('shop-detail')
    class Meta:
        model = Shop
        fields = ['id','name','address','changed_timestamp','address','url']