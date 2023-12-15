from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from rest_framework import status, response
from .models import Product
from .serializers import ProductSerializer
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class ProductViewSet(ViewSet):
    # permission_classes=[IsAuthenticated]

    def list(self,request):
        query = Product.objects.all()
        product = ProductSerializer(query,many=True)
        return response.Response(product.data,status=status.HTTP_200_OK)
