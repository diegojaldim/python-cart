class Product:
    
    def __init__(self, name, price, qty):
        self.name = name
        self.price = price
        self.qty = qty

    def apply_discount(self, percentage):
        self.price -= (self.price * percentage) / 100