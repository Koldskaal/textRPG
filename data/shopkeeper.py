import shopkeeper_stock
import sys

class Shop:
    def __init__(self):
        self.menu_options = ["buy", "sell", "leave"]
        self.menu_position = 0
        self.shop_position = 0

    def shop_menu(self, direction):
        """ direction is :"""
        print(shopkeeper_stock.shop_items)
        if self.menu_position == 0:
            print(colored("Buy", 'on_green', attrs=['bold']))
            print("Sell")
            print("Leave Shop")
            if direction == "ENTER":
                buy_item()
            if direction == "s":
                self.menu_position += 1
            else:
                pass
        if self.menu_position == 1:
            print("Buy"))
            print(colored("Sell", 'on_green', attrs=['bold']))
            print("Leave Shop")
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
                leave_shop()
                if direction == "w":
                self.menu_position -= 1
            else:
                pass


def stock(self):
    self.stock

def

def buy_item():
    pass

def sell_item():
    pass

def leave_shop():
