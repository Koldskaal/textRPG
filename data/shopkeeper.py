from . import shopkeeper_stock
import sys
from . import room

class Shop:
    def __init__(self):
        self.menu_options = ["buy", "sell", "leave"]
        self.menu_position = 0
        self.shop_position = 0
        self.trade_position = 0

    def print_room(self):
        if self.menu_position == 0:
            print(shopkeeper_stock.shop_items)
            print(colored("Buy", 'on_green', attrs=['bold']))
            print("Sell")
            print("Leave Shop")
        if self.menu_position == 1:
            print("Buy")
            print(colored("Sell", 'on_green', attrs=['bold']))
            print("Leave Shop")
        if self.menu_position == 2:
            print("Buy")
            print("Sell")
            print(colored("Leave Shop", 'on_green', attrs=['bold']))


    def shop_menu(self, direction):
        """ direction is :"""
        if self.menu_position == 0:
            if direction == "ENTER":
                buy_item()
            if direction == "s":
                self.menu_position += 1
            else:
                pass
        if self.menu_position == 1:
            if direction == "ENTER":
                sell_item()
            if direction == "s":
                self.menu_position += 1
            if direction == "w":
                self.menu_position -= 1
            else:
                pass
        if self.menu_position == 2:
            print("Buy")
            print("Sell")
            print(colored("Leave Shop", 'on_green', attrs=['bold']))
            if direction == "ENTER":
                room.leave_shop()
            if direction == "w":
                self.menu_position -= 1
            else:
                pass


def stock(self):
    pass

#def

def buy_item(bought):
        if self.trade_position == 0:
            if direction == "ENTER":
                shopkeeper_stock.shop_items.del(bought)
                #-gold
            if direction == "s":
                self.menu_position += 1
            else:
                pass
        if self.trade_position > 0:
            if direction == "ENTER":
                shopkeeper_stock.shop_items.del(bought)
                #-gold
            if direction == "s":
                self.menu_position += 1
            if direction == "w":
                self.menu_position -= 1
            else:
                pass
        if self.trade_position == len(shopkeeper_stock.shop_items):
            if direction == "ENTER":
                shopkeeper_stock.shop_items.del(bought)
                #-gold
            if direction == "w":
                self.menu_position -= 1
            else:
                pass

def sell_item():
    pass
