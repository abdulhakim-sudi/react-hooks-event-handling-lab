import pytest
from customer import Customer
from coffee import Coffee
from order import Order

def test_customer_name_validation():
    with pytest.raises(ValueError):
        Customer("")  # name too short
    with pytest.raises(ValueError):
        Customer("A"*16)  # name too long

def test_create_order_and_orders_method():
    cust = Customer("Alice")
    coffee = Coffee("Latte")
    order = cust.create_order(coffee, 3.5)

    assert isinstance(order, Order)
    assert order.customer == cust
    assert order.coffee == coffee
    assert order.price == 3.5

    orders = cust.orders()
    assert order in orders

def test_coffees_method():
    cust = Customer("Bob")
    coffee1 = Coffee("Espresso")
    coffee2 = Coffee("Mocha")
    cust.create_order(coffee1, 2.5)
    cust.create_order(coffee2, 3.0)
    coffees = cust.coffees()
    assert coffee1 in coffees
    assert coffee2 in coffees
