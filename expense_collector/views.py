from decimal import Decimal
from django.http import HttpResponse, Http404

from .models import Transaction, Tag


def hello(request):
    return HttpResponse('Hello world')


def create_transaction(request):
    if request.method == 'POST':
        transaction = Transaction.objects.create(
            name=request.POST.get('name'),
            amount=Decimal(request.POST.get('amount')),
            type=request.POST.get('type'),
            description=request.POST.get('description'))
        transaction.save()

        tags_list = request.POST.get('tags').split('|||')
        
        for tag in tags_list:
            current_tag = Tag.objects.filter(name=tag)
            if current_tag.count() > 0:
                transaction.tags.add(current_tag)
            else:
                new_tag = Tag.objects.create(name=tag)
                new_tag.save()
                transaction.tags.add(new_tag)
            transaction.save()
        return HttpResponse('OK')
    else:
        raise Http404()