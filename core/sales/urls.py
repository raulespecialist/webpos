from django.urls import path
from . import views

urlpatterns = [
    path('', views.InvoiceListView.as_view({'get': 'list'}), name='invoice_list'),
]