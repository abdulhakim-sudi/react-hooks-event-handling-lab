import pytest
from customer import Customer
from coffee import Coffee
from order import Order

def test_order_initialization():
    cust = Customer("Frank")
    coffee = Coffee("Flat White")
    order = Order(cust, coffee, 3.5)

    assert order.customer == cust
    assert order.coffee == coffee
    assert order.price == 3.5

def test_order_price_validation():
    cust = Customer("Grace")
    coffee = Coffee("Macchiato")
    with pytest.raises(ValueError):
        Order(cust, coffee, 0.5)  # price too low
    with pytest.raises(ValueError):
        Order(cust, coffee, 15.0)  # price too high
