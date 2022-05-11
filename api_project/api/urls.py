from django.urls import path,include
from . import views

# API endpoints

urlpatterns = [
    path('',views.api_root),
    path(
        'addresses/',
        views.AddressList.as_view(),
        name='addr-list'
        ),
    path(
        'addresses/<int:pk>/',
        views.AddressDetail.as_view(),
        name='addr-detail'
        ),
    path(
        'shops/',
        views.ShopList.as_view(),
        name='shop-list'
        ),
    path(
        'shops/<int:pk>/',
        views.ShopDetail.as_view(),
        name='shop-detail'
        ),
]