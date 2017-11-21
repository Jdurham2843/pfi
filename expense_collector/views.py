from decimal import Decimal
from django.http import HttpResponse, Http404

from .models import Transaction, Tag


# Create Transaction View + helpers    
def create_transaction_controller(request):
    if request.method == 'POST':
        transaction = create_transaction(request)

        tags_list = request.POST.get('tags').split('|||')
        
        if tags_list:
            add_tags_to_transaction(transaction, tags_list)
        return HttpResponse('OK')
    else:
        raise Http404()


def create_transaction(request):
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
            transaction.save()