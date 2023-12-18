from rest_framework.viewsets import ViewSet
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import Product,Category
from .serializers import ProductSerializer,CategorySerializer
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class ProductViewSet(ViewSet):
    permission_classes=[IsAuthenticated]

    def retrieve(self,request,pk=None):
        query = Product.objects.get(id=pk)
        product = ProductSerializer(query)
        return Response(product.data,status=status.HTTP_200_OK)
    
    def create(self,request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def partial_update(self,request,pk=None):
        query = Product.objects.get(id=pk)
        serializer = ProductSerializer(query,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class ProductsView(APIView):
    permission_classes=[IsAuthenticated]
    def get(self,request):
        query = Product.objects.all()
        product = ProductSerializer(query,many=True)
        return Response(product.data,status=status.HTTP_200_OK)

class CategoryViewSet(ViewSet):
    permission_classes=[IsAuthenticated]

    def retrieve(self,request,pk=None):
        query = Category.objects.get(id=pk)
        category = CategorySerializer(query)
        return Response(category.data,status=status.HTTP_200_OK)
    
    def create(self,request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def update(self,request,pk=None):
        query = Category.objects.get(id=pk)
        serializer = CategorySerializer(query,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class CategoriesView(APIView):
    permission_classes=[IsAuthenticated]
    def get(self,request):
        query = Category.objects.all()
        product = CategorySerializer(query,many=True)
        return Response(product.data,status=status.HTTP_200_OK)