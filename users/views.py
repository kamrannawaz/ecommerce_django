from rest_framework import viewsets,views
from rest_framework import status
from rest_framework.response import Response
from .models import Cart,User
from store.models import Product
from .serializers import CartSerializer, UserSerializer,UserSignUpSerializer
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class UserView(views.APIView):
    permission_classes=[IsAuthenticated]
    def get(self,request):
        if request.user.is_admin:
            query = User.objects.all()
            users = UserSerializer(query,many=True)
            return Response(users.data,status=status.HTTP_200_OK)
        return Response({'message':'not allowed'},status=status.HTTP_400_BAD_REQUEST)

class UserCreateView(views.APIView):
    def post(self,request):
        username = request.data['username']
        email = request.data['email']
        try:
            email = User.objects.get(email=email)
            username = User.objects.get(username=username)

            if email or username:
                return Response({'error':'username or email already exists'},status=status.HTTP_400_BAD_REQUEST)
        except:
            pass
        try:
            user = UserSignUpSerializer(data=request.data)
            if user.is_valid():
                user.save()
                newUser=user.data
                del newUser['password']
                return Response(newUser,status=status.HTTP_201_CREATED)
        except:
            return Response({'error':user.errors},status=status.HTTP_400_BAD_REQUEST)

class UserViewSet(viewsets.ViewSet):
    permission_classes=[IsAuthenticated]
    def retrieve(self,request,pk=None):
        query = User.objects.get(id=pk)
        users = UserSerializer(query)
        return Response(users.data,status=status.HTTP_200_OK)
    
class CartViewSet(viewsets.ViewSet):
    permission_classes=[IsAuthenticated]

    def list(self,request):
        query = Cart.objects.filter(user=request.user)
        cart = CartSerializer(query,many=True)
        return Response(cart.data,status=status.HTTP_200_OK)
    
    def create(self,request):
        serializer = CartSerializer(data=request.data)
        if serializer.is_valid():
            product = Product.objects.get(id=request.data['product'])
            if not request.data.get('quantity',None):
                request.data['quantity']=1
            if product.quantity < request.data['quantity']:
                return Response({'error':'not enough stock'},status=status.HTTP_400_BAD_REQUEST)
            product.quantity -= request.data['quantity']
            product.save()

            cart = Cart.objects.filter(user=request.user,product=request.data['product'])
            if cart:
                cart[0].quantity += request.data['quantity']
                cart[0].save()
                query = Cart.objects.filter(user=request.user)
                cart = CartSerializer(query,many=True)
                return Response(cart.data,status=status.HTTP_201_CREATED)

            serializer.save(user=request.user)
            query = Cart.objects.filter(user=request.user)
            cart = CartSerializer(query,many=True)
            return Response(cart.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

    
    