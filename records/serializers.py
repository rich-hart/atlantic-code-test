from rest_framework import serializers

from .models import Document, Customer 

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ('upload',)

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('id','first_name','last_name')

