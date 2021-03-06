""" Views for expense_collector """

from django.http import Http404, HttpResponseRedirect, HttpResponseBadRequest
from django.shortcuts import render
from django.urls import reverse

from .services import transaction_service


def index_view(request):
    return render(request, 'pfi/index.html', {})


def create_transaction_view(request):
    if request.method == 'POST':
        try:
            transaction_request = {
                'name': request.POST['name'],
                'type': request.POST['type'],
                'amount': request.POST['amount'],
                'description': request.POST.get('description', ''),
                'tags': request.POST.get('tags', '').split(',')
            }
            transaction_service.create_transaction(transaction_request)
        except Exception:
            raise Http404()
        else:
            return HttpResponseRedirect(reverse('create_transaction_view'))
    elif request.method == 'GET':
        return render(request, 'pfi/create_transaction.html', {})
    else:
        return HttpResponseBadRequest()


def remove_transaction_view(request, uuid):
    if request.method == 'POST':
        remove_request = {
            'uuid': uuid
        }

        try:
            transaction_service.remove_transaction(remove_request)
        except Exception:
            raise Http404()
        else:
            return HttpResponseRedirect(reverse('index_view'))
    else:
        return HttpResponseBadRequest()
