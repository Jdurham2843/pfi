from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^create-transaction$', views.create_transaction_view,
        name='create_transaction_view'),
    url(r'(?P<uuid>[^/]+)/remove-transaction', views.remove_transaction_view,
        name='remove_transaction_view'),
    url(r'index', views.index_view, name='index_view')
]
