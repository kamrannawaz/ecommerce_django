from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from rest_framework import status, response
from .models import Cart,User
from .serializers import CartSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class CartViewSet(ViewSet):
    permission_classes=[IsAuthenticated]

    def list(self,request):
        query = Cart.objects.all()
        cart = CartSerializer(query,many=True)
        return response.Response(cart.data,status=status.HTTP_200_OK)


class UserViewSet(ViewSet):
    permission_classes=[IsAuthenticated]
    def list(self,request):
        query = User.objects.all()
        users = UserSerializer(query,many=True)
        return response.Response(users.data,status=status.HTTP_200_OK)