""" Expense Collector Models """
from django.db import models
from django.utils import timezone

import uuid as uid


class Tag(models.Model):
    uuid = models.UUIDField(default=uid.uuid4, editable=False)
    name = models.CharField(max_length=255, unique=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class TransactionSet(models.Model):
    uuid = models.UUIDField(default=uid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=400)
    tags = models.ManyToManyField(Tag, related_name="transaction_set")
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True) 
    transaction_set_date = models.DateTimeField(default=timezone.now, blank=True)


class Transaction(models.Model):
    DEBIT = 'DB'
    CREDIT = 'CR'

    TRANSACTION_TYPE_CHOICES = (
        (DEBIT, 'Debit'),
        (CREDIT, 'Credit'),
    )

    uuid = models.UUIDField(default=uid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    type = models.CharField(
        max_length=2,
        choices=TRANSACTION_TYPE_CHOICES,
    )
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=400)
    transaction_set = models.ForeignKey(TransactionSet, on_delete=models.CASCADE, blank=True, null=True)
    tags = models.ManyToManyField(Tag, related_name="transaction")
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    transaction_date = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self):
        return '<{type}: {name} ${amount} -- \"{description}\">'.format(
            self.type, self.name, self.amount, self.description
        )
    
    class Meta:
        ordering = ('name', 'type', 'amount', 'description',)