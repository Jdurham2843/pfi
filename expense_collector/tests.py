from django.test import TestCase
from .models import Transaction, Tag

# Create your tests here.
class DebitTests(TestCase):
    def test_add_debit_to_collector(self):
        pass
    
    def test_retrieve_debit_from_collector(self):
        new_debit = Transaction.objects.create(
            name="Eggs",
            type=Transaction.DEBIT,
            price=0.52,
            description="eggs have protein"
        )
        new_debit.save()

        for item in ['eggs', 'grocery']:
            new_tag = Tag.objects.create(name=item)
            new_tag.save()
            new_tag.transactions.add(new_debit)
            new_tag.save()

    def test_update_transaction(self):
        pass
    
    def test_remove_transaction(self):
        pass