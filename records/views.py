import csv
import codecs
from django.shortcuts import render
from rest_framework import viewsets

from .models import Document, Customer, Address, Product, Record
from .serializers import DocumentSerializer, CustomerSerializer, AddressSerializer, ProductSerializer, RecordSerializer

class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

    def perform_create(self, serializer):
#        import ipdb; ipdb.set_trace()
        instance = serializer.save()
        buffer_fp = codecs.iterdecode(instance.upload, 'utf-8') 
        reader = csv.reader(buffer_fp, delimiter='\t')
        document = instance
        for row in reader:
            customer, _ = Customer.objects.update_or_create(id=row[0],first_name=row[1],last_name=row[2])
            address, _ = Address.objects.update_or_create(street=row[3],state=row[4],zip_code=row[5])
            product, _ = Product.objects.update_or_create(id=row[7], name=row[8], amount=row[9])
            record = Record.objects.create(
                document=document,
                customer=customer,
                address=address,
                product=product,
                status=row[6].upper()[0],
                timestamp=row[10]
            )

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class RecordViewSet(viewsets.ModelViewSet):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
