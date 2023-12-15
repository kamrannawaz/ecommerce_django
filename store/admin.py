from django.contrib import admin
from .models import Product
# Register your models here.

class ShowID(admin.ModelAdmin):
    readonly_fields=['id']

admin.site.register(Product,ShowID)