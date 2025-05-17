class Coffee:
    def __init__(self, name: str):
        self.name = name
        self._orders = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Coffee name must be a string.")
        if len(value) < 3:
            raise ValueError("Coffee name must be at least 3 characters long.")
        self._name = value

    def _add_order(self, order):
        self._orders.append(order)

    def orders(self):
        return self._orders

    def customers(self):
        # Return unique Customers who ordered this coffee
        return list({order.customer for order in self._orders})

    def num_orders(self):
        return len(self._orders)

    def average_price(self):
        if not self._orders:
            return 0.0
        total = sum(order.price for order in self._orders)
        return total / len(self._orders)
