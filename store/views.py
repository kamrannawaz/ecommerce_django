from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from rest_framework import status, response
from .models import Product,Category
from .serializers import ProductSerializer,CategorySerializer
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class ProductViewSet(ViewSet):
    permission_classes=[IsAuthenticated]

    def list(self,request):
        query = Product.objects.all()
        product = ProductSerializer(query,many=True)
        return response.Response(product.data,status=status.HTTP_200_OK)


class CategoryViewSet(ViewSet):
    permission_classes=[IsAuthenticated]

    def list(self,request):
        query = Category.objects.all()
        category = CategorySerializer(query,many=True)
        return response.Response(category.data,status=status.HTTP_200_OK)