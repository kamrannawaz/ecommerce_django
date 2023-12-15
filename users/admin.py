from django.contrib import admin
from .models import User,Cart,WishList

# Register your models here.

class ShowID(admin.ModelAdmin):
    readonly_fields=['id']

admin.site.register([User,Cart,WishList],ShowID)
