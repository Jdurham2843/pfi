from decimal import Decimal

from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.db import IntegrityError, transaction
from django.urls import reverse

from .models import Transaction, Tag


# Create Transaction View + helpers
def create_transaction_view(request):
    if request.method == 'POST':
        try:
            transaction = create_transaction(request)
        except IntegrityError:
            raise Http404()

        try:
            tags_list = request.POST.get('tags').split('|||')
        except Exception:
            pass
        else:
            if tags_list:
                add_tags_to_transaction(transaction, tags_list)
        finally:
            return HttpResponseRedirect(reverse('create_transaction_view'))
    elif request.method == 'GET':
        return render(request, 'pfi/index.html', {})


@transaction.atomic
def create_transaction(request):
    """ Helper function to create Transaction object """
    transaction = Transaction.objects.create(
            name=request.POST.get('name'),
            amount=Decimal(request.POST.get('amount')),
            type=request.POST.get('type'),
            description=request.POST.get('description'))

    return transaction


def add_tags_to_transaction(transaction, tags_list):
    for tag in tags_list:
            current_tag = Tag.objects.filter(name=tag)
            if current_tag.count() > 0:
                transaction.tags.add(current_tag)
            else:
                new_tag = Tag.objects.create(name=tag)
                transaction.tags.add(new_tag)