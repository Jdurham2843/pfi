""" Service to retrive transaction related objects """
from decimal import Decimal

from django.db import transaction

from ..models import Transaction, Tag


@transaction.atomic
def create_transaction(request):
    transaction = Transaction.objects.create(
            name=request['name'],
            amount=Decimal(request['amount']),
            type=request['type'],
            description=request['description'])
    
    if request['tags']:
        add_tags_to_transaction(transaction, request['tags'])


def add_tags_to_transaction(transaction, tags_list):
    for tag in tags_list:
            current_tag = Tag.objects.filter(name=tag)
            if current_tag.count():
                transaction.tags.add(current_tag)
            else:
                new_tag = Tag.objects.create(name=tag)
                transaction.tags.add(new_tag)


def remove_transaction(request):
    transaction = Transaction.objects.get(uuid=request['uuid'])
    if transaction:
        transaction.delete()
    else:
        raise Exception('Transaction does not exist')