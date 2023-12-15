from rest_framework.routers import SimpleRouter
from django.urls import path,include
from .views import CartViewSet,UserViewSet

router = SimpleRouter()
router.register(r'cart',CartViewSet,basename='cart')
router.register(r'users',UserViewSet,basename='user')

urlpatterns = [
    path('',include(router.urls))
]