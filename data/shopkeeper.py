from . import shopkeeper_stock
import sys
from . import room
from termcolor import colored

class Shop:
    def __init__(self, canvas):
        self.canvas = canvas
        self.menu_options = ["Buy", "Sell", "Leave"]
        self.menu_position = 0
        self.shop_position = 0
        self.trade_position = 0

    def print_room(self):
        self.pre_index = self.menu_options[0:self.menu_position]
        self.index = colored(self.menu_options[self.menu_position], "white", 'on_green', attrs=['bold'])
        self.post_index =  self.menu_options[self.menu_position+1:]
        self.canvas.add_to_print("room", "\n".join(self.pre_index) + "\n" + self.index + "\n" + "\n".join(self.post_index))
        self.canvas.print_canvas()

    def shop_menu(self, direction):
        """ direction is :"""
        if direction is "s":
            self.menu_position += 1
            if self.menu_position > 2:
                self.menu_position = 2
            self.print_room()
        if direction is "w":
            self.menu_position -= 1
            if self.menu_position <0:
                self.menu_position = 0
            self.print_room()
<<<<<<< HEAD
        if direction is "e":
=======
        if direction is '\r': # ENTER KEY
>>>>>>> 04f55406e70df47a4f4f9495e2b8e74b132df747
            if self.menu_position == 0:
                self.buy_item()
            if self.menu_position == 1:
                self.sell_item()
            if self.menu_position == 2:
                self.leave_shop()

def stock(self):
    pass

def leave_shop(self):
    room_controller.RoomController().leave_shop()

def buy_item(self):
        bought = self.trade_position
        if self.trade_position == 0:
            if direction == "ENTER":
                del shopkeeper_stock.shop_items[bought]
                #-gold
            if direction == "s":
                self.menu_position += 1
            else:
                pass
        if self.trade_position > 0:
            if direction == "ENTER":
                del shopkeeper_stock.shop_items[bought]
                #-gold
            if direction == "s":
                self.menu_position += 1
            if direction == "w":
                self.menu_position -= 1
            else:
                pass
        if self.trade_position == len(shopkeeper_stock.shop_items):
            if direction == "ENTER":
                del shopkeeper_stock.shop_items[bought]
                #-gold
            if direction == "w":
                self.menu_position -= 1
            else:
                pass

def sell_item():
    pass
