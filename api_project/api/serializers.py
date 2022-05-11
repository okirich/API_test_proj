from rest_framework import serializers
from .models import Address,Shop

class AddressSerializer(serializers.ModelSerializer):
    shops = serializers.HyperlinkedRelatedField(
        many=True,
        # read_only=True
        queryset=Shop.objects.all(),
        view_name='shop-detail'
        )
    url = serializers.HyperlinkedIdentityField('addr-detail')
    class Meta:
        model = Address
        fields = ['id','street','building','shops','url']

class ShopSerializer(serializers.ModelSerializer):
    address = serializers.HyperlinkedRelatedField(
        many=False,
        queryset=Address.objects.all(), 
        view_name='addr-detail'
    )
    url = serializers.HyperlinkedIdentityField('shop-detail')
    class Meta:
        model = Shop
        fields = ['id','name','address','changed_timestamp','address','url']