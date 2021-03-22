from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound

from .models import Sale
from .serializers.common import SaleSerializer


class SaleListView(APIView):

    def get(self, _request):
        sales = Sale.objects.all()
        serialized_sales = SaleSerializer(sales, many=True)
        return Response(serialized_sales.data, status=status.HTTP_200_OK)

    def post(self, request):
        sale_to_create = SaleSerializer(data=request.data)
        if sale_to_create.is_valid():
            sale_to_create.save()
            return Response(sale_to_create.data, status=status.HTTP_201_CREATED)
        return Response(sale_to_create.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)


class SaleDetailView(APIView):

    def get_sale(self, pk):
        try:
            return Sale.objects.get(pk=pk)
        except Sale.DoesNotExist:
            raise NotFound()

    def get(self, _request, pk):
        sale = self.get_sale(pk=pk)
        serialized_sale = SaleSerializer(sale)
        return Response(serialized_sale.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        sale_to_update = self.get_sale(pk=pk)
        updated_sale = SaleSerializer(sale_to_update, data=request.data)
        if updated_sale.is_valid():
            updated_sale.save()
            return Response(updated_sale.data, status=status.HTTP_202_ACCEPTED)
        return Response(updated_sale.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    def delete(self, _request, pk):
        sale_to_delete = self.get_sale(pk=pk)
        sale_to_delete.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
