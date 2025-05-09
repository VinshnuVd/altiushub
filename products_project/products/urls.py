from products.views import ProductCreateList, ProductDetailUpdateDelete
from django.urls import path

urlpatterns = [
    path('', ProductCreateList.as_view(), name='product-list-create'),
    path('<int:pk>/', ProductDetailUpdateDelete.as_view(), name='product-detail-update-delete'),
]