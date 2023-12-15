from django.shortcuts import render
from rest_framework import viewsets,views
from rest_framework import status
from rest_framework.response import Response
from .models import Cart,User
from .serializers import CartSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class CartViewSet(viewsets.ViewSet):
    permission_classes=[IsAuthenticated]

    def list(self,request):
        query = Cart.objects.all()
        cart = CartSerializer(query,many=True)
        return Response(cart.data,status=status.HTTP_200_OK)

class UserView(views.APIView):
    permission_classes=[IsAuthenticated]
    def get(self,request):
        if request.user.is_admin:
            query = User.objects.all()
            users = UserSerializer(query,many=True)
            return Response(users.data,status=status.HTTP_200_OK)
        return Response({'message':'not allowed'},status=status.HTTP_400_BAD_REQUEST)

class UserViewSet(viewsets.ViewSet):
    permission_classes=[IsAuthenticated]
    def retrieve(self,request,pk=None):
        query = User.objects.get(id=pk)
        users = UserSerializer(query)
        return Response(users.data,status=status.HTTP_200_OK)