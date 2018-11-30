from rest_framework import serializers

from .models import Document, Customer, Address, Product

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ('upload',)

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('id','first_name','last_name')

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ('street','state','zip_code')

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'amount') 
