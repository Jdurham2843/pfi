from decimal import Decimal

from django.test import TestCase, Client

from .models import Transaction, Tag

# Create your tests here.
class DebitTests(TestCase):
    def setUp(self):
        self.client = Client()
    
    def create_example_debit(self):
        new_debit = Transaction.objects.create(
            name="Eggs",
            type=Transaction.DEBIT,
            price=0.52,
            description="eggs have protein"
        )
        new_debit.save()

        egg_tag = Tag.objects.create(name='Egg')
        egg_tag.save()
        grocery_tag = Tag.objects.create(name='Grocery')
        grocery_tag.save()

        new_debit.tags.add(egg_tag)
        new_debit.tags.add(grocery_tag)

    def test_add_debit_to_collector(self):
        response = self.client.post('/create-transaction', data={
            'name': 'Eggs',
            'price': '0.52',
            'type': 'DB',
            'description': 'Eggs have protein',
            'tags': ['Eggs', 'Grocery'],
        })

        self.assertEqual(response.status_code, 200)

        added_debit = Transaction.objects.first()
        self.assertEqual(added_debit.name, 'Eggs')
        self.assertEqual(added_debit.price, Decimal('0.52'))
        self.assertEqual(added_debit.type, 'DB')
        self.assertEqual(added_debit.description, 'Eggs have protein')
        
        self.assertTrue(len(Transaction.objects.filter(tags__name='Eggs') == 1))
    
    def test_retrieve_debit_from_collector(self):
        new_debit = self.create_example_debit()


    def test_update_transaction(self):
        pass
    
    def test_remove_transaction(self):
        pass