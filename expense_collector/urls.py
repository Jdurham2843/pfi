from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.hello, name='hello'),
    url(r'^create-transaction$', views.create_transaction,
        name='create_transaction'),
]
