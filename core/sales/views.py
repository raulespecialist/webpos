from django.shortcuts import render
from .models import Invoice, Item
from rest_framework import viewsets
from django.db.models import Prefetch
from rest_framework.decorators import action
from .serializers import InvoiceListSerializer, ItemListSerializer, InvoiceSerializer
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 1000


class InvoiceListView(viewsets.ModelViewSet):
    serializer_class = InvoiceListSerializer
    queryset = Invoice.objects.prefetch_related('code_number')
    pagination_class = StandardResultsSetPagination

    def get_serializer_class(self):
        if self.action == 'list':
            return InvoiceListSerializer
        return InvoiceSerializer

    def get_queryset(self):
        queryset = Invoice.objects.all()
        '''
        queryset = Invoice.objects.prefetch_related(Prefetch(
        'status'))
        '''

        if self.request.GET.get('created_date'):
            queryset = queryset.filter(created_date=self.request.GET.get('created_date'))
        if self.request.GET.get('status'):
            queryset = queryset.filter(status=self.request.GET.get('status'))
        if self.request.GET.get('pay_type'):
            queryset = queryset.filter(pay_type=self.request.GET.get('pay_type'))
        else:
            queryset = queryset.order_by('-created_date')
        return queryset

    def list(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    #def create(self, request):
