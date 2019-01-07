import shopkeeper_stock
menu_options = ["buy", "sell", "leave"]
menu_position = 0

def shop_menu():
    while True
        print(shopkeeper_stock.shop_items)
        if menu_position == 0:
            if event.name == "ENTER":
                buy_item()
            if event.name == "s":
                menu_position += 1
            else:
                pass
        if menu_position == 1:
            if event.name == "ENTER":
                sell_item()
            if event.name == "s":
                menu_position += 1
            if event.name == "w":
                menu_position -= 1
            else:
                pass
        if menu_position == 2:
            if event.name == "ENTER":
                leave_shop()

            if event.name == "w":
                menu_position -= 1
            else:
                pass


def stock(self):

def buy_item():
    pass

def sell_item():
    pass

def leave_shop():
