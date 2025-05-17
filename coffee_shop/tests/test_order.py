import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from customer import Customer
from coffee import Coffee
from order import Order

def test_order_price_validation():
    c = Customer("Test")
    coffee = Coffee("Brew")
    o = Order(c, coffee, 5.0)
    assert o.price == 5.0
