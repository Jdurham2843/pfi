""" Views for expense_collector """

from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.db import IntegrityError
from django.urls import reverse

from .services import transaction_service


# Create Transaction View + helpers
def create_transaction_view(request):
    if request.method == 'POST':
        try:
            transaction = transaction_service.create_transaction(request)
        except IntegrityError:
            raise Http404()

        try:
            tags_list = request.POST.get('tags').split('|||')
        except Exception:
            pass
        else:
            if tags_list:
                transaction_service.add_tags_to_transaction(transaction,
                                                            tags_list)
        finally:
            return HttpResponseRedirect(reverse('create_transaction_view'))
    elif request.method == 'GET':
        #TODO: build out transaction html page
        return render(request, 'pfi/index.html', {})
