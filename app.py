from product import Product
from item import Item

ps5_with_discount = Product('Playstation 5', 4999.50)
ps5_with_discount.discount_percentage = 20
ps5_with_discount.apply_discount()

item1 = Item(ps5_with_discount, 4)
item1_total_value = item1.get_total_value()

print(item1_total_value)