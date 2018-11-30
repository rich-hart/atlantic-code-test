from django.db import models
from enum import Enum


class Document(models.Model):
    upload = models.FileField()


class Customer(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)


class Address(models.Model):
    street = models.CharField(max_length = 255)
    state = models.CharField(max_length = 2)
    zip_code = models.CharField(max_length = 5)


class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length = 100)
    amount = models.DecimalField(max_digits=12, decimal_places = 2)


class Record(models.Model):
    class Status(Enum):
        New = 'N'
        Cancelled = 'C'
        @classmethod
        def get_choices(cls):
            return [(e.value, e.name) for _, e in enumerate(cls)]

    document = models.ForeignKey('Document', on_delete=models.DO_NOTHING)
    customer = models.ForeignKey('Customer', on_delete=models.DO_NOTHING)
    address = models.ForeignKey('Address', on_delete=models.DO_NOTHING)
    product = models.ForeignKey('Product', on_delete=models.DO_NOTHING)
    status = models.CharField(
        max_length = 1,
        choices = Status.get_choices(),
        default = Status.New.value,
    )
    timestamp = models.DateTimeField()


