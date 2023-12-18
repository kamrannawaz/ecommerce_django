import uuid
from django.db import models
from django.contrib.auth.models import  AbstractUser
from store.models import Product
# Create your models here.


class User(AbstractUser):
    id=models.UUIDField(primary_key=True,blank=False,default=uuid.uuid4,editable=False)
    username=models.CharField(max_length=100,blank=False,editable=False, unique=True)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    contact=models.CharField(max_length=11)
    is_admin=models.BooleanField(default=False,editable=False)
    email = models.EmailField(max_length=70,blank=False,unique=True)

    USERNAME_FIELD='username'

    def __str__(self):
        return self.username
    

class Address(models.Model):
    id=models.UUIDField(primary_key=True,blank=False,default=uuid.uuid4,editable=False)
    user=models.ForeignKey(User,related_name='user_addresses',on_delete=models.CASCADE,blank=True)
    street=models.CharField(max_length=100)
    city=models.CharField(max_length=100)

    def __str__(self):
        return f'{self.user.username}'

class Cart(models.Model):
    id=models.UUIDField(primary_key=True,blank=False,default=uuid.uuid4,editable=False)
    user=models.ForeignKey(User,related_name='user_cart',on_delete=models.CASCADE,null=False)
    quantity=models.IntegerField(default=1)
    product=models.ForeignKey(Product, related_name='product_cart',on_delete=models.CASCADE,null=False)

    def __str__(self):
        return str(self.id)
    
class WishList(models.Model):
    id=models.UUIDField(primary_key=True,blank=False,default=uuid.uuid4,editable=False)
    user=models.ForeignKey(User,related_name='user_wish_list',on_delete=models.CASCADE,blank=False)
    product=models.ForeignKey(Product, related_name='product_wish_list',on_delete=models.CASCADE,blank=False)

    def __str__(self):
        return str(self.id)

 




    
