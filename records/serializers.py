from rest_framework import serializers

from .models import Document, Customer, Address, Product, Record

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ('upload',)

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('id','first_name','last_name')
        read_only_fields = fields

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ('street','state','zip_code')
        read_only_fields = fields

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'amount')
        read_only_fields = fields

class RecordSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Record
        fields = ('document','customer','address','product','status','timestamp')
        read_only_fields = fields
