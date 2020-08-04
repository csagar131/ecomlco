from django.urls import path,include
from rest_framework import routers
from .views import OrderViewSet, add


router = routers.DefaultRouter()
router.register('', OrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('add/<str:id>/<str:token>/', add),
]