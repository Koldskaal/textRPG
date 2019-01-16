from . import basic_menu, game_log, talents
from random import sample
from termcolor import colored

class TalentMenu(basic_menu.BasicRotatingMenu):
    def __init__(self):
        super().__init__()

        self.title = 'Info'
        self.menu_options = self.get_three_random_talents_from_pile()

    def get_three_random_talents_from_pile(self):
        three_talents = sample(talents.talent_list, 3)
        return three_talents

    def define_descriptions(self, item):
        return item.descrition, None

    def print_room(self, clear=False):

        settings = {
            'column_priority'  : 2,     # Order of who goes first from left to right
            'delay'             : 3,     # if it needs to be x lines below
            'width'             : 41,    # how wide will it print
            'allignment'        : '^',
            'max_lines'         : 15,    # for the string that keeps getting bigger. Take only the latest 30
            'join_char'         : '',
            'title'             : 'CHOOSE-A-TALENT',
            'push'              : 0
        }
        if len(self.menu_options) == 0:
            self.canvas.add_to_print("room", "", settings)
            self.canvas.print_canvas(clear)
            self.description_box(True)
        else:
            max = len(self.menu_options)
            if max > 9: max = 9
            aft_num = max // 2
            bef_num = max - aft_num


            before = "\n".join(talent.name for talent in self.menu_options[-aft_num:]) + '\n'
            temp = list(talent.name for talent in self.menu_options[:bef_num])
            if len(self.menu_options) > 1:
                hover = colored(self.menu_options[0].name, "white", 'on_green')
                new = before + "\n".join(temp).replace(temp[0], hover, 1)
            else:
                new = ' \n' + colored(before, "white", 'on_green', attrs=['bold'])

            self.canvas.add_to_print("room",new ,settings)
            self.canvas.print_canvas(clear)
            self.description_box()

    def exit(self):
        return
