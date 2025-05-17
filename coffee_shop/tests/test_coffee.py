import pytest
from coffee import Coffee
from customer import Customer

def test_coffee_name_validation():
    with pytest.raises(ValueError):
        Coffee("aa")  # less than 3 chars

def test_orders_and_customers_methods():
    coffee = Coffee("Cappuccino")
    cust1 = Customer("Charlie")
    cust2 = Customer("Dana")
    cust1.create_order(coffee, 4.0)
    cust2.create_order(coffee, 3.5)

    orders = coffee.orders()
    customers = coffee.customers()

    assert len(orders) == 2
    assert cust1 in customers
    assert cust2 in customers

def test_num_orders_and_average_price():
    coffee = Coffee("Americano")
    cust = Customer("Eve")
    cust.create_order(coffee, 3.0)
    cust.create_order(coffee, 5.0)

    assert coffee.num_orders() == 2
    assert coffee.average_price() == 4.0
