import csv
import codecs
from django.shortcuts import render
from rest_framework import viewsets

from .models import Document
from .serializers import DocumentSerializer

class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

    def perform_create(self, serializer):
#        import ipdb; ipdb.set_trace()
        instance = serializer.save()
        buffer_fp = codecs.iterdecode(instance.upload, 'utf-8') 
        reader = csv.reader(buffer_fp, delimiter='\t')
        for row in reader:
            print(row)
