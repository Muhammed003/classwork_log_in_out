from rest_framework import status
from django.db.models import Q
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from .models import Product
from .serializers import ProductSerializer, ProductCRUDSerializer

""" First method """
# class ProductListView(ListAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     permission_classes = (IsAuthenticated,)
#
#
#
# class ProductListCreateAPIView(ListCreateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     permission_classes = (IsAuthenticated,)
#
#
# class ProductUpdateAPIView(UpdateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     permission_classes = (IsAuthenticated,)
#
#
# class ProductDestroyAPIView(DestroyAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     permission_classes = (IsAuthenticated,)

""" Second method """


class ProductAPIView(APIView):
    def get(self, request):
        search = request.query_params.get("search")
        order_by = request.query_params.get("order_by")
        if order_by:
            products = Product.objects.order_by(order_by)
        else:
            if search:
                products = Product.objects.filter(Q(title__icontains=search) | Q(desc__icontains=search),
                                                  is_published=True)
            else:
                products = Product.objects.filter(is_published=True)

        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProductSetView(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductCRUDSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        print(self.request.user)
        return super().get_queryset()
