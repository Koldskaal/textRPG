""" This scrpit is supposed to tie all objects together to a single print """
import colorama
import termcolor
import ansiwrap
try:
    from .textures import *
except ModuleNotFoundError:
    from textures import *

class Canvas:
    def __init__(self):
        self.areas = {}
        self.border = True
        self.default_settings = {
            'column_priority'  : 1,     # Order of who goes first from left to right
            'delay'             : 0,     # if it needs to be x lines below
            'width'             : 30,    # how wide will it print
            'allignment'        : '^',
            'max_lines'         : 0,    # for the string that keeps getting bigger. Take only the latest 30
            'join_char'         : '',
            'push'              : 30
        }


        self.gap = 1

    def add_to_print(self, name, string, settings={}):
        self.areas[name] = settings
        self.areas[name]['string'] = string

    def replace_line(self, name, string, line):
        if ansiwrap.ansilen(string) > self.areas[name]['width']:
            string = ansiwrap.wrap(string, self.areas[name]['width'])[0]
        if not self.areas[name].get('replace'):
            self.areas[name]['replace'] = [(string, line)]
        else:
            if any(line in c for c in self.areas[name]['replace']):
                self.areas[name]['replace'] = [(string, line)]
            else:
                self.areas[name]['replace'].append((string,line))

    def popup(self, name, string, start_position, title=None):
        s = string.splitlines()
        wrap = []
        for line in s:
            wrap += ansiwrap.wrap(line, self.areas[name].get('width', 30)-2)
        top = BORDER_INLINE * self.areas[name].get('width', 30) if not title else title.upper().center(self.areas[name].get('width', 30), BORDER_INLINE)
        box = [top,]
        box += wrap
        box.append(BORDER_INLINE * self.areas[name].get('width', 30))

        self.areas[name]['popup'] = [box, start_position]

    def print_canvas(self, clear=False):
        # Find the lowest printed line
        popup = {}
        lines = 0
        for items in self.areas.values():
            items['_split'] = items['string'].splitlines()
            wrap = []
            for i in items['_split']:
                wrap += ansiwrap.wrap(i, items.get('width', 30))
            items['_split'] = wrap
            if len(items['_split']) > items.get('max_lines', 0) and items.get('max_lines', 0) != 0:
                items['_split'] = items['_split'][-items['max_lines']:]


            temp_lines = len(items['_split']) + items.get('delay', 0)
            if temp_lines > lines:
                lines = temp_lines
            if lines < items.get('max_lines', 0):
                lines = items.get('max_lines', 0)

        def create_allignment(s, width, allignment):
            needed = width - ansiwrap.ansilen(s)
            if needed > 0:
                if allignment == '>' or allignment == 'right':
                    return needed * ' ' + s
                elif allignment == '<' or allignment == 'left':
                    return s + needed * ' '
                elif allignment == '^' or allignment == 'middle':
                    s = (needed//2) * ' ' + s + (needed//2) * ' '
                    if ansiwrap.ansilen(s) < width:
                        s = ' ' + s
                    return s
            else:
                return s


        kyk = ''
        # print in order
        # find the horizontal order
        def takeSecond(elem):
            return elem[1]
        list_of_columns = []
        for k in self.areas.keys():
            list_of_columns.append((k,self.areas[k].get('column_priority', 100)))
        list_of_columns.sort(key=takeSecond)

        big_string = ""
        start_postition = {}
        for i in range(lines+2):
            big_string +="\n"
            for k, useless in list_of_columns:
                if i == 0 and self.border:
                    mid = '{:{char}{a}{w}}'.format(self.areas[k].get('title', ''), char=BORDER_UP_DOWN, w=self.areas[k].get('width', 30), a='^')
                    big_string+=(' '*self.gap + BORDER_CORNER_UP_LEFT + mid  + BORDER_CORNER_UP_RIGHT)
                elif i == lines+1 and self.border:
                    big_string+=' '*self.gap + BORDER_CORNER_DOWN_LEFT + BORDER_UP_DOWN*self.areas[k].get('width', 30) + BORDER_CORNER_DOWN_RIGHT
                else:
                    # print(self.areas[k].get('replace', []))
                    if any(i in c for c in self.areas[k].get('replace', [])):
                        for line in self.areas[k].get('replace'):
                            if line[1] == i:
                                kyk = create_allignment(line[0], self.areas[k].get('width', 30), self.areas[k].get('allignment', '^'))
                                if self.border:
                                    kyk =' '*self.gap +  BORDER_LEFT_RIGHT + kyk + BORDER_LEFT_RIGHT
                                big_string += kyk
                    elif i >= self.areas[k].get('popup', [0,0])[1] and self.areas[k].get('popup', [0,0])[0] and not popup.get(k, [0,0])[1]:
                        if not popup.get(k):
                            popup[k] = [self.areas[k].get('popup', [])[0].copy(), False]
                        popped = self.areas[k].get('popup', [])[0].pop(0)
                        if not self.areas[k]['popup'][0] and not popup[k][1]:
                            self.areas[k]['popup'][0] = popup[k][0].copy()
                            popup[k][1] = True
                        if popped:
                            if self.areas[k].get('push'):
                                popped = ' ' * self.areas[k].get('push') + popped
                            add = create_allignment(popped, self.areas[k].get('width', 30), self.areas[k].get('allignment', '^'))
                            if self.border:
                                add =' '*self.gap +  BORDER_LEFT_RIGHT + add + BORDER_LEFT_RIGHT
                            big_string += add
                    elif i >= self.areas[k].get('delay', 0):
                        popped = self.areas[k]['_split'].pop(0) if self.areas[k]['_split'] else ' '
                        if popped:
                            if self.areas[k].get('push'):
                                popped = ' ' * self.areas[k].get('push') + popped
                            add = create_allignment(popped, self.areas[k].get('width', 30), self.areas[k].get('allignment', '^'))
                            if self.border:
                                add =' '*self.gap +  BORDER_LEFT_RIGHT + add + BORDER_LEFT_RIGHT
                            big_string += add


                    # elif i <= self.areas[k].get('max_lines', 0) and self.areas[k].get('max_lines', 0) != 0:
                    #     big_string += (' '*self.gap + BORDER_LEFT_RIGHT + ' ' * self.areas[k].get('width', 30) + BORDER_LEFT_RIGHT  if self.border else ' ' * self.areas[k].get('width', 30))
                    else:
                        big_string += (' '*self.gap + BORDER_LEFT_RIGHT + ' ' * self.areas[k].get('width', 30) + BORDER_LEFT_RIGHT if self.border else ' ' * self.areas[k].get('width', 30))



        print("\033[H")
        if clear:
            print("\033[H\033[J")

        print(big_string)
        # print(popup.get('room'))


    def print_example(self):
        height = 10
        width = 10
        self.main_box = []
        for x in range(height):
            self.main_box.append(["x"]*width)

        for x in range(height):
            y = 1
            while y<width-1:
                if x != 0 and x != height-1:
                    self.main_box[x][y] = " "
                y = y+1
        self.main_box[3][3] = 'P'



        string = ""
        healthbox = """----------------[u]-
 Health: 100/100
 Mana:   100/100
 Str:    10+4(14)
 Int:    10
 Agi:    10
----------------[i]-
 Equipment:
    - Helmet
    - Boots
    ...
--------------------
-------------------------------------------------------------------
"""

        print("This is how it could look.")
        s = ''
        for row in self.main_box:
            s += '\n'
            s += " ".join(row)

        # print(s)
        self.add_to_print('room', termcolor.colored(s, 'red'), {'column_priority': 1, 'width': 40})
        self.add_to_print('stats', healthbox, {'column_priority': 2, 'width': 20, 'allignment': '<', 'delay': 1})
        self.add_to_print('room2', s, {'column_priority': 3, 'width': 40, 'delay': 5})
        self.popup('room2', 'you are amemsda asd dasd', 10, 'title')
        self.replace_line('room', 'asdasd', 2)
        self.print_canvas()

    """
        # IDEA: Takes in dictionaries, like so:
        {
            'column_priority'  : 1     # Order of who goes first from left to right
            'string'            : 'This is what will get printed and split to lines'
            'delay'             : 0     # if it needs to be x lines below
            'width'             : 30    # how wide will it print
            (optional thoughts)
            'allignment'        : < , > or ^ for the format
            'max_lines'         : 30    # for the string that keeps getting bigger. Take only the latest 30

        }

        it needs some kind of identifier so it is updateable.


    """
if __name__ == '__main__':
    c = Canvas().print_example()
