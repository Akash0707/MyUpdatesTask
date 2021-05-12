from django.test import TestCase
from .calc import add, subtract

class calcTests(TestCase):
    def test_add_numbers(self):
        "Test two number are addes together"
        self.assertEqual(add(3,8), 11)
    
    def test_subtract_numbers(self):
        self.assertEqual(subtract(5,11),6)

