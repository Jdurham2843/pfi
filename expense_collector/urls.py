from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^create-transaction$', views.create_transaction_view,
        name='create_transaction_view'),
]
