from rest_framework.routers import SimpleRouter
from django.urls import path,include
from .views import ProductViewSet,CategoryViewSet

router = SimpleRouter()
router.register(r'product',ProductViewSet,basename='product')
router.register(r'category',CategoryViewSet,basename='category')

urlpatterns = [
    path('',include(router.urls))
]