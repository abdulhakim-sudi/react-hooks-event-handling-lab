class Customer:
    def __init__(self, name: str):
        self.name = name
        self._orders = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Customer name must be a string.")
        if not (1 <= len(value) <= 15):
            raise ValueError("Customer name must be between 1 and 15 characters.")
        self._name = value

    def orders(self):
        return self._orders

    def coffees(self):
        # Return unique Coffee instances from the orders
        return list({order.coffee for order in self._orders})

    def create_order(self, coffee, price):
        from order import Order  # delayed import to avoid circular
        order = Order(self, coffee, price)
        self._orders.append(order)
        coffee._add_order(order)
        return order
