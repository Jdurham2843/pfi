""" Expense Collector Models """
from django.db import models
import uuid

class TransactionSet(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=400)

class Transaction(models.Model):
    DEBIT = 'DB'
    CREDIT = 'CR'

    TRANSACTION_TYPE_CHOICES = (
        (DEBIT, 'Debit'),
        (CREDIT, 'Credit'),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    type = models.CharField(
        max_length=2,
        choices=TRANSACTION_TYPE_CHOICES,
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=400)

    def __str__(self):
        return '<{type}: {name} ${price} -- \"{description}\">'.format(
            self.type, self.name, self.price, self.description
        )
    
    class Meta:
        ordering = ('name', 'type', 'price', 'description',)


class Tag(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, unique=True)
    transactions = models.ManyToManyField(Transaction)
    transaction_sets = models.ManyToManyField(TransactionSet)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
