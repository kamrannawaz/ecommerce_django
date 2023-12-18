from rest_framework import serializers
from .models import Cart,User

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cart
        fields="__all__"



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
