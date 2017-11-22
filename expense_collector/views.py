""" Views for expense_collector """

from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .services import transaction_service


# Create Transaction View + helpers
def create_transaction_view(request):
    if request.method == 'POST':
        try:
            transaction_service.create_transaction(request)
        except Exception:
            raise Http404()
        else:
            return HttpResponseRedirect(reverse('create_transaction_view'))
    elif request.method == 'GET':
        # TODO: build out transaction html page
        return render(request, 'pfi/index.html', {})
