from django.urls import path
from .views import ProductApiViewset, ProductApiViewOthers, ProductAnalytics

urlpatterns = [
    path('product/', ProductApiViewset.as_view()),
    path('product/<int:pk>/', ProductApiViewOthers.as_view()),
    path('products/popluar/<str:time>', ProductAnalytics.as_view())
]

