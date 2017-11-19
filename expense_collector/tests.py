from decimal import Decimal

from django.test import TestCase, Client

from .models import Transaction


# Create your tests here.
class DebitTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_add_debit_to_collector(self):
        response = self.client.post('/expense/create-transaction', data={
            'name': 'Eggs',
            'type': 'DB',
            'amount': '0.52',
            'description': 'Eggs have protein',
            'tags': 'Eggs|||Grocery'
        })

        self.assertEqual(response.status_code, 200)

        added_debit = Transaction.objects.first()
        self.assertEqual(added_debit.name, 'Eggs')
        self.assertEqual(added_debit.amount, Decimal('0.52'))
        self.assertEqual(added_debit.type, 'DB')
        self.assertEqual(added_debit.description, 'Eggs have protein')
        
        self.assertEqual(Transaction.objects.filter(tags__name='Eggs').count(), 1)
    
    def test_retrieve_debit_from_collector(self):
        pass

    def test_update_transaction(self):
        pass
    
    def test_remove_transaction(self):
        pass