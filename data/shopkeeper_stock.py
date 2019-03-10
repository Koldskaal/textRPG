from random import choice
from . import item_ID

shop_items= []

for stock in range(30):
    shop_items.append(choice(list(item_ID.items.keys())))
