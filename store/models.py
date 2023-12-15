from django.db import models
import uuid
# Create your models here.

class Category(models.Model):
    id=models.UUIDField(primary_key=True,blank=False,default=uuid.uuid4,editable=False)
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    id=models.UUIDField(primary_key=True,blank=False,default=uuid.uuid4,editable=False)
    name=models.CharField(max_length=100)
    category=models.ForeignKey(Category,related_name='product_category',on_delete=models.CASCADE,blank=False)
    price=models.FloatField(default=0.0)
    discount=models.FloatField(default=0.0)
    quantity=models.IntegerField(default=0)

    def __str__(self):
        return self.name
    