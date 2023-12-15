from rest_framework import serializers
from .models import Cart,User

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cart
        fields="__all__"



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields="__all__"