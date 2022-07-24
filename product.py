class Product:
    
    discount_percentage = 0

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def apply_discount(self):
        if (self.discount_percentage > 0):
            self.price -= (self.price * self.discount_percentage) / 100
            return 