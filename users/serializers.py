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