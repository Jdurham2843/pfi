from decimal import Decimal

from django.test import TestCase, Client

from .models import Transaction, Tag


# Create your tests here.
class TransactionTests(TestCase):
    def setUp(self):
        self.client = Client()
    
    def generate_data(self):
        return {
            'name': 'Eggs',
            'type': 'DB',
            'amount': '0.52',
            'description': 'Eggs have protein',
            'tags': 'Eggs,Grocery'
        }
    
    def generate_data_no_tags(self):
        return {
            'name': 'Eggs',
            'type': 'DB',
            'amount': '0.52',
            'description': 'Eggs have protein',
        }
    
    def generate_invalid_data(self):
        return {
            'name2': 'Eggs',
            'type': 'DB',
            'amount': '0.52',
            'description': 'Eggs have protein',
        }
    
    def generate_transaction(self):
        transaction = Transaction.objects.create(name='Eggs',
                                                 type='DB',
                                                 amount='0.52',
                                                 description='protein')
        
        for tag in ('Eggs', 'Grocery'):
            new_tag = Tag.objects.create(name=tag)
            transaction.tags.add(new_tag)
        transaction.save()

    def test_add_valid_debit_to_collector(self):
        response = self.client.post('/expense/create-transaction', 
                                    self.generate_data())

        self.assertEqual(response.status_code, 302)

        added_debit = Transaction.objects.first()
        self.assertEqual(added_debit.name, 'Eggs')
        self.assertEqual(added_debit.amount, Decimal('0.52'))
        self.assertEqual(added_debit.type, 'DB')
        self.assertEqual(added_debit.description, 'Eggs have protein')
        
        self.assertEqual(Transaction.objects.filter(tags__name='Eggs').count(), 1)
    
    def test_add_no_tag_debit_to_collector(self):
        response = self.client.post('/expense/create-transaction', 
                                    self.generate_data_no_tags())

        self.assertEqual(response.status_code, 302)

        added_debit = Transaction.objects.first()
        self.assertEqual(added_debit.name, 'Eggs')
        self.assertEqual(added_debit.amount, Decimal('0.52'))
        self.assertEqual(added_debit.type, 'DB')
        self.assertEqual(added_debit.description, 'Eggs have protein')
        
        self.assertEqual(Transaction.objects.filter(tags__name='Eggs').count(), 0)
    
    def test_add_invalid_debit_to_collector(self):
        response = self.client.post('/expense/create-transaction', 
                                    self.generate_invalid_data())

        self.assertEqual(response.status_code, 404)
        self.assertEqual(Transaction.objects.count(), 0)
    
    def test_retrieve_debit_from_collector(self):
        pass

    def test_update_transaction(self):
        pass
    
    def test_remove_transaction(self):
        self.generate_transaction()
        transaction = Transaction.objects.first()
        transaction_uuid = transaction.uuid
        
        response = self.client.post(
              '/expense/{uuid}/remove-transaction'.format(
                  uuid=transaction_uuid))
        
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Transaction.objects.filter(uuid=transaction_uuid))