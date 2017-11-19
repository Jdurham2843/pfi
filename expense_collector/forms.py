""" File containing forms for expense collector """
from django import forms

from .models import Transaction


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ('name', 'type', 'amount', 'description')