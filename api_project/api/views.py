import imp
import django
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.response import Response
from .models import Address,Shop
from .serializers import AddressSerializer,ShopSerializer
from django.http import JsonResponse, response
from rest_framework.status import HTTP_201_CREATED 

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

    def perform_create(self, serializer):
        serializer.save()
        response = JsonResponse(
            {'id':serializer.data['id']},
            status=HTTP_201_CREATED)
        print(response.content)
        return response

class AddressDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

class ShopList(generics.ListCreateAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer

    def perform_create(self, serializer):
        serializer.save()
        response = JsonResponse(
            {'id':serializer.data['id'],
            'name':serializer.data['name']},
            status=HTTP_201_CREATED)
        print(response.content)
        return response

class ShopDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
