from customer import Customer
from coffee import Coffee
from order import Order

c1 = Customer("Ali")
c2 = Customer("Zoe")
latte = Coffee("Latte")
mocha = Coffee("Mocha")

c1.create_order(latte, 3.5)
c1.create_order(mocha, 4.0)
c2.create_order(latte, 5.0)

print(f"{c1.name}'s Orders:", c1.orders())
print(f"{latte.name} has {latte.num_orders()} orders.")
print(f"Aficionado for {latte.name}:", Customer.most_aficionado(latte).name)
