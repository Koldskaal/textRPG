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
            'alignment'        : '^',
            'max_lines'         : 0,    # for the string that keeps getting bigger. Take only the latest 30
            'join_char'         : '',
            'push'              : 30
        }


        self.gap = 1

    @staticmethod
    def create_alignment(s, width, alignment):
        needed = width - ansiwrap.ansilen(s)
        if needed > 0:
            if alignment == '>' or alignment == 'right':
                return needed * ' ' + s
            elif alignment == '<' or alignment == 'left':
                return s + needed * ' '
            elif alignment == '^' or alignment == 'middle':
                s = (needed//2) * ' ' + s + (needed//2) * ' '
                if ansiwrap.ansilen(s) < width:
                    s = ' ' + s
                return s
        else:
            return s

    def add_to_print(self, name, string, settings={}, replace=True):
        if replace:
            self.areas[name] = settings
        self.areas[name]['string'] = string

    def replace_line(self, name, string, line, clear=False):
        if ansiwrap.ansilen(string) > self.areas[name]['width']:
            string = ansiwrap.wrap(string, self.areas[name]['width'])[0]
        # print(self.areas[name]['string'])
        if not self.areas[name].get('replace') or clear:

            self.areas[name]['replace'] = [(string, line)]
        else:
            if any(line in c for c in self.areas[name]['replace']):
                # print(f'replace with {string}')s
                self.areas[name]['replace'] = [(string, line) if x[1] == line else x for x in self.areas[name]['replace']]
                # print(self.areas[name]['replace'])
            else:
                # print(f'append with {string}')
                self.areas[name]['replace'].append((string,line))

    def replace_line_specific(self, name, string, line, spot, clear=False):
        if not self.areas[name].get('replace_specific') or clear:
            self.areas[name]['replace_specific'] = [(string, line, spot)]
        else:
            if any(line in c for c in self.areas[name]['replace_specific']):
                spots = [] # to check if spot is taken.
                for x in self.areas[name]['replace_specific']:
                    spots.append(x[2])
                if spot not in spots:
                    self.areas[name]['replace_specific'].append((string,line, spot))
            else:
                self.areas[name]['replace_specific'].append((string,line, spot))

    def popup(self, name, string, start_position, title=None, stats=None, alignment='^'):
        s = string.splitlines()
        wrap = []
        for line in s:
            wrap += ansiwrap.wrap(line, self.areas[name].get('width', 30)-2)
        top = BORDER_INLINE * self.areas[name].get('width', 30) if not title else title.upper().center(self.areas[name].get('width', 30), BORDER_INLINE)
        box = [top,]
        box += wrap
        if stats:
            box.append(BORDER_INLINE_THIN * self.areas[name].get('width', 30))
            stat = ""
            for k, v in stats.items():
                stat += f"{k.upper()}: {v} | "
            stat = self.create_alignment(stat[:-3], self.areas[name].get('width', 30), alignment)
            box.append(stat)
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
                                kyk = self.create_alignment(line[0], self.areas[k].get('width', 30), self.areas[k].get('alignment', '^'))
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
                            add = self.create_alignment(popped, self.areas[k].get('width', 30), self.areas[k].get('alignment', '^'))
                            if self.border:
                                add =' '*self.gap +  BORDER_LEFT_RIGHT + add + BORDER_LEFT_RIGHT
                            big_string += add
                    elif i >= self.areas[k].get('delay', 0):
                        popped = self.areas[k]['_split'].pop(0) if self.areas[k]['_split'] else ' '
                        if popped:
                            if self.areas[k].get('push'):
                                popped = ' ' * self.areas[k].get('push') + popped
                            add = self.create_alignment(popped, self.areas[k].get('width', 30), self.areas[k].get('alignment', '^'))
                            if self.border:
                                add =' '*self.gap +  BORDER_LEFT_RIGHT + add + BORDER_LEFT_RIGHT
                            big_string += add


                    # elif i <= self.areas[k].get('max_lines', 0) and self.areas[k].get('max_lines', 0) != 0:
                    #     big_string += (' '*self.gap + BORDER_LEFT_RIGHT + ' ' * self.areas[k].get('width', 30) + BORDER_LEFT_RIGHT  if self.border else ' ' * self.areas[k].get('width', 30))
                    else:
                        big_string += (' '*self.gap + BORDER_LEFT_RIGHT + ' ' * self.areas[k].get('width', 30) + BORDER_LEFT_RIGHT if self.border else ' ' * self.areas[k].get('width', 30))
                    if any(i in c for c in self.areas[k].get('replace_specific', [])):
                        for line in self.areas[k].get('replace_specific'):
                            if line[1] == i:
                                count = 0
                                stripped = len(ansiwrap.strip_color(big_string.splitlines()[-1])) - self.areas[k].get('width', 30)

                                while True:
                                    unstripped = big_string[-(self.areas[k].get('width', 30)+count):]
                                    if len(ansiwrap.strip_color(big_string.splitlines()[-1].replace(unstripped,''))) == stripped:
                                        break
                                    count += 1

                                zero_point = len(big_string) -  len(unstripped) - 1

                                big_string_list = list(big_string)
                                first_part = line[2][0] if line[2][0] < 0 else zero_point+line[2][0]
                                second_part = line[2][1] if line[2][1] < 0 else zero_point+line[2][1]

                                big_string_list[first_part:second_part] = list(line[0])
                                big_string = "".join(big_string_list)



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
        self.add_to_print('stats', healthbox, {'column_priority': 2, 'width': 20, 'alignment': '<', 'delay': 1})
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
            'alignment'        : < , > or ^ for the format
            'max_lines'         : 30    # for the string that keeps getting bigger. Take only the latest 30

        }

        it needs some kind of identifier so it is updateable.


    """
if __name__ == '__main__':
    c = Canvas().print_example()
