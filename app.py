from product import Product

ps5 = Product('Playstation 5', 4999.50, 1)
ps5.apply_discount(20)

print(ps5.price)