from rest_framework.routers import SimpleRouter
from django.urls import path,include
from .views import ProductViewSet

router = SimpleRouter()
router.register(r'product',ProductViewSet,basename='product')

urlpatterns = [
    path('',include(router.urls))
]