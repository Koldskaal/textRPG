class menu:
    def __init__(self, canvas):
        self.canvas = canvas
        self.menu_options = []#"index1","index2","index3"
        self.menu_position = 0

    def print_room(self, clear=False):
        self.pre_index = self.menu_options[0:self.menu_position]
        self.index = colored(self.menu_options[self.menu_position], "white", 'on_green', attrs=['bold'])
        self.post_index =  self.menu_options[self.menu_position+1:]
        self.canvas.add_to_print("room", "\n".join(self.pre_index) + "\n" + self.index + "\n" + "\n".join(self.post_index))
        self.canvas.print_canvas()

    def shop_menu(self, direction):
        """ direction is :"""
        if direction is "s":
            self.menu_position += 1
            #if self.menu_position > 2:
                #self.menu_position = 2
            self.print_room()
        if direction is "w":
            self.menu_position -= 1
            #if self.menu_position <0:
                #self.menu_position = 0
            self.print_room()
        if direction is "ENTER":
            if self.menu_position == 0:
                pass
            if self.menu_position == 1:
                pass
            if self.menu_position == 2:
                pass
