from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.response import Response
from .models import Address,Shop
from .serializers import AddressSerializer,ShopSerializer

# Create your views here.

@api_view(['GET'])
def api_root(request):
    return Response({
            'addresses': reverse('addr-list',request=request),
            'shops':reverse('shop-list',request=request)
        })

class AddressList(generics.ListCreateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer 

class AddressDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

class ShopList(generics.ListCreateAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer

class ShopDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
