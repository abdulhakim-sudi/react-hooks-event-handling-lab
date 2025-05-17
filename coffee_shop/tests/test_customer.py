import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from customer import Customer
from coffee import Coffee

def test_customer_name():
    c = Customer("Abdi")
    assert c.name == "Abdi"

def test_create_order():
    c = Customer("Zara")
    coffee = Coffee("Espresso")
    o = c.create_order(coffee, 5.0)
    assert o.customer == c
    assert o.coffee == coffee
