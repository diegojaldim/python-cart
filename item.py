from product import Product

class Item:

    def __init__(self, product, qty):
        self.product = product
        self.qty = qty


    def get_total_value(self):
        return self.product.price * self.qty

    