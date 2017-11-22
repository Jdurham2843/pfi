""" Service to retrive transaction related objects """
from decimal import Decimal

from django.db import transaction
from ..models import Transaction, Tag


@transaction.atomic
def create_transaction(request):
    """ Helper function to create Transaction object """
    transaction = Transaction.objects.create(
            name=request['name'],
            amount=Decimal(request['amount']),
            type=request['type'],
            description=request['description'])
    
    try:
        tags_list = request['tags'].split('|||')
    except Exception:
        pass
    else:
        add_tags_to_transaction(transaction, tags_list)


def add_tags_to_transaction(transaction, tags_list):
    for tag in tags_list:
            current_tag = Tag.objects.filter(name=tag)
            if current_tag.count() > 0:
                transaction.tags.add(current_tag)
            else:
                new_tag = Tag.objects.create(name=tag)
                transaction.tags.add(new_tag)