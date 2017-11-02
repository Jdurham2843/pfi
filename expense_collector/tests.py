from django.test import TestCase
from .models import Debit

# Create your tests here.
class DebitTests(TestCase):
    def test_add_debit_to_collector(self):
        pass
    
    def test_retrieve_debit_from_collector(self):
        new_debit = Debit.objects.create(name="Eggs", price=0.52, description="eggs have protein")
        new_debit.save()

        ret_debit = Debit.objects.first()

        self.assertEqual(ret_debit.name, "Eggs")
        self.assertEqual(format(ret_debit.price, '.2f'), '0.52')
        #self.assertEqual(ret_debit.tags, ["grocery", "eggs"])
        self.assertEqual(ret_debit.description, "eggs have protein")



    
    def test_update_debit_to_collector(self):
        pass
    
    def test_remove_debit_from_collector(self):
        pass