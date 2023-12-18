from rest_framework import serializers
from .models import Cart,User
from store.models import Product

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cart
        fields="__all__"

class CartItemAddRemoveSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cart
        fields=['product','quantity','id']

    def create(self,validate_data):
        user = self.context['request'].user
        product = Product.objects.get(id=validate_data['product'].id)
        
        if product.quantity < validate_data['quantity']:
            raise serializers.ValidationError('Out of stock')
        product.quantity -= validate_data['quantity']
        product.save(force_update=True)

        cart_item = Cart.objects.filter(user=user,product=product.id).first()
        if cart_item:
            cart_item.quantity += validate_data['quantity']
            cart_item.save()
            return cart_item
        
        cart = Cart.objects.create(
            user=user,
            product=validate_data['product'],
            quantity=validate_data['quantity']
        )
        cart.save()
        return cart


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','username','first_name','last_name','email','is_admin','contact','user_addresses','user_cart','user_wish_list']
    
    def create(self,validate_data):
        user = User.objects.create(
            email=validate_data['email'],
            username=validate_data['username']
        )

        user.set_password(validate_data['password'])

        user.save()
        return user

class UserSignUpSerializer(serializers.Serializer):
    id=serializers.UUIDField(read_only=True)
    email=serializers.EmailField(max_length=70,required=True)
    username=serializers.CharField(max_length=100,required=True)
    password=serializers.CharField(max_length=100,required=True)
    first_name=serializers.CharField(max_length=100,required=True)
    last_name=serializers.CharField(max_length=100,required=True)

    def create(self,validate_data):
            user = User.objects.create(
                email=validate_data['email'],
                username=validate_data['username'],
                first_name=validate_data['first_name'],
                last_name=validate_data['last_name']
            )

            user.set_password(validate_data['password'])
            user.save()
            return user
