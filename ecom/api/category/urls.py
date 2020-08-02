from django.urls import path,include
from rest_framework import routers
from .views import CategoryModelViewset

router = routers.DefaultRouter()
router.register('', CategoryModelViewset)

urlpatterns = [
    path('', include(router.urls)),
]