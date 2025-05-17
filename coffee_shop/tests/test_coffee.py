import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from customer import Customer
from coffee import Coffee
from order import Order

def test_coffee_average_price():
    coffee = Coffee("Cappuccino")
    c1 = Customer("A")
    c2 = Customer("B")
    Order(c1, coffee, 4.0)
    Order(c2, coffee, 6.0)
    assert coffee.average_price() == 5.0
