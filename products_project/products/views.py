# Create your views here.
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import FilterSet

from products.models import Product
from products.serializers import ProductSerializer
from products_project.paginator import CustomPaginator
from products.filters import ProductFilter



class ProductCreateList(GenericAPIView):
    query_set = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = CustomPaginator
    filter_backends = [DjangoFilterBackend]
    filteset_class = ProductFilter
    # filterset_fields = ['name', 'rent', 'address', 'no_of_bedrooms', 'posted_on']

    def get_queryset(self):
        query_set = Product.objects.filter(is_deleted=False).order_by('-posted_on')
        return query_set
    

    def get(self, request):
        try:
            query_set = self.get_queryset()
            if request.path != '/home/':
                query_set = query_set.filter(is_deleted=False)
                filtered_queryset = self.filter_queryset(self.get_queryset())
                paginated_queryset = self.paginate_queryset(filtered_queryset)
                serializer = ProductSerializer(paginated_queryset, many=True)
                paginated_response = self.get_paginated_response(serializer.data)
                return paginated_response
            else:
                serializer = ProductSerializer(query_set, many=True)
            return render(request, 'home.html', context={'products': serializer.data})
        except Exception as e:
            print("Exception in get method: ", e)
            return Response({
                'status': '500',
                'message': 'Internal Server Error'
            }, status=500)
        
    def post(self, request):
        try:
            data = request.data
            serializer = ProductSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'status': '201',
                    'message': 'Product Created Successfully'
                }, status=201)
            else:
                return Response({
                    'status': '400',
                    'message': serializer.errors
                }, status=400)
        # except JSONParser as e:
        #     return Response({
        #         'status': '400',
        #         'message': 'Invalid JSON'
        #     }, status=400)
        except Exception as e:
            print("Exception in post method: ", e)
            return Response({
                'status': '500',
                'message': 'Internal Server Error'
            }, status=500)
        

class ProductDetailUpdateDelete(GenericAPIView):

    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk, is_deleted=False)
        except Product.DoesNotExist:
            return None
    def get(self, pk):
        try:
            product = self.get_object(pk)
            if product is not None:
                serializer = ProductSerializer(product)
                return Response({
                    'status': '200',
                    'data': serializer.data
                }, status=200)
            else:
                return Response({
                    'status': '404',
                    'message': 'Product Not Found'
                }, status=404)
        except Exception as e:
            return Response({
                'status': '500',
                'message': 'Internal Server Error'
            }, status=500)
        

    def put(self, request, pk):
        try:
            product = self.get_object(pk)
            if product is not None:
                serializer = ProductSerializer(product, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response({
                        'status': '200',
                        'message': 'Product Updated Successfully'
                    }, status=200)
                else:
                    return Response({
                        'status': '400',
                        'message': serializer.errors
                    }, status=400)
            else:
                return Response({
                    'status': '404',
                    'message': 'Product Not Found'
                }, status=404)
        except Exception as e:
            return Response({
                'status': '500',
                'message': 'Internal Server Error'
            }, status=500)
        

    def delete(self, request, pk):
        try:
            product = self.get_object(pk)
            if product is not None:
                product.is_deleted = True
                product.save()
                return Response({
                    'status': '200',
                    'message': 'Product Deleted Successfully'
                }, status=200)
            else:
                return Response({
                    'status': '404',
                    'message': 'Product Not Found'
                }, status=404)
        except Exception as e:
            return Response({
                'status': '500',
                'message': 'Internal Server Error'
            }, status=500)