from django.urls import path,include

urlpatterns = [
    path('category/', include('api.category.urls')),
    path('products/', include('api.product.urls')),
]