from .models import Invoice, Item
from rest_framework import serializers


class ItemListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('invoice', 'code_number', 'name', 'quantity', 'unit_price', 'sum_price')


class InvoiceListSerializer(serializers.ModelSerializer):

    """
    code_number = serializers.SerializerMethodField()

    def get_code_number(self, invoice):

        qs = Item.objects.filter(invoice_id=invoice.id)#.order_by('update_date')
        serializer = ItemListSerializer(instance=qs, many=True)
        return serializer.data
    """
    
    #items = ItemListSerializer(many=True, read_only=True, source='item_set')

    class Meta:
        model = Invoice
        fields = '__all__'


class InvoiceSerializer(serializers.ModelSerializer):
    items = ItemListSerializer(many=True, read_only=True, source='item_set')

    class Meta:
        model = Invoice
        fields = '__all__'
