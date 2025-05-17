import pytest
from customer import Customer
from coffee import Coffee

def test_customer_name_validation():
    with pytest.raises(ValueError):
        Customer("")

    with pytest.raises(ValueError):
        Customer("a" * 16)

def test_create_order_and_relationships():
    c = Customer("Alice")
    coffee = Coffee("Latte")
    order = c.create_order(coffee, 3.5)
    assert order.customer == c
    assert order.coffee == coffee
    assert order.price == 3.5
    assert order in c.orders()
    assert order in coffee.orders()
    assert coffee in c.coffees()
    assert c in coffee.customers()
