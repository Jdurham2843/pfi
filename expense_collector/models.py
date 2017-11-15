""" Expense Collector Models """
from django.db import models
import uuid

class Tag(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)

class TransactionSet(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=400)
    tags = models.ManyToManyField(Tag, related_name="transaction_set")

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
    transaction_set = models.ForeignKey(TransactionSet, on_delete=models.CASCADE, default=None)
    tags = models.ManyToManyField(Tag, related_name="transaction")

    def __str__(self):
        return '<{type}: {name} ${price} -- \"{description}\">'.format(
            self.type, self.name, self.price, self.description
        )
    
    class Meta:
        ordering = ('name', 'type', 'price', 'description',)