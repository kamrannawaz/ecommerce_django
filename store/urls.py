from rest_framework.routers import SimpleRouter
from django.urls import path,include
from .views import ProductViewSet,CategoryViewSet,ProductsView,CategoriesView

router = SimpleRouter()
router.register(r'product',ProductViewSet,basename='product')
router.register(r'category',CategoryViewSet,basename='category')

urlpatterns = [
    path('products/',ProductsView.as_view()),
    path('categories/',CategoriesView.as_view()),
    path('',include(router.urls))
]