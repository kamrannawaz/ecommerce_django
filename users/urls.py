from rest_framework.routers import SimpleRouter
from django.urls import path,include
from .views import CartViewSet,UserViewSet,UserView,UserCreateView

router = SimpleRouter()
router.register(r'cart',CartViewSet,basename='cart')
router.register(r'user',UserViewSet,basename='user')

urlpatterns = [
    path('users/',UserView.as_view()),
    path('user/',UserCreateView.as_view()),
    path('',include(router.urls))
]