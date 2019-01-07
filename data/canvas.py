""" This scrpit is supposed to tie all objects together to a single print """

class Canvas:
    def __init__(self):
        self.areas = {}

        self.default_settings = {
            'horizontal_order'  : 1,     # Order of who goes first from left to right
            'delay'             : 0,     # if it needs to be x lines below
            'width'             : 30,    # how wide will it print
            'allignment'        : '^',
            'max_lines'         : 0,    # for the string that keeps getting bigger. Take only the latest 30
            'join_char'         : ''
        }

    def add_to_print(self, name, string, settings={}):
        self.areas[name] = settings
        self.areas[name]['string'] = string

    def print_canvas(self):
        # Check for the lowest line
        lines = 0
        for items in self.areas.values():
            items['_split'] = items['string'].splitlines()
            if len(items['_split']) > items.get('max_lines', 0) and items.get('max_lines', 0) != 0:
                items['_split'] = items['_split'][-items['max_lines']:]
            fills = len(items['_split']) + items.get('delay', 0)
            if fills > lines:
                lines = fills

        # print in order
        # find the horizontal order
        def takeSecond(elem):
            return elem[1]
        list_of_columns = []
        for k in self.areas.keys():
            list_of_columns.append((k,self.areas[k].get('horizontal_order', 100)))

        list_of_columns.sort(key=takeSecond)

        big_string = ""
        for i in range(lines):
            print("outs")
            big_string += '\n'
            for k, useless in list_of_columns:
                if i >= self.areas[k].get('delay', 0):
                    popped = self.areas[k]['_split'].pop(0) if self.areas[k]['_split'] else ''
                    if popped:
                        big_string += '{: {allignment}{width}}|'.format(
                            f"{self.areas[k].get('join_char', '')}".join(popped),
                            allignment = self.areas[k].get('allignment', '^'),
                            width = self.areas[k].get('width', 30)
                        )
                        print('in')

        print(big_string)



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
        healthbox = """--------------------
 Health: 100/100
 Mana:   100/100
 Str:    10+4(14)
 Int:    10
 Agi:    10
--------------------
 Equipment:
    - Helmet
    - Boots
    ...
--------------------"""


        # lines = max(len(self.main_box), len(healthbox))
        # nr = 40
        # for i in range(lines):
        #     string += "\n" + '{: ^{nr}}|{: <20}|'.format(
        #
        #     " ".join(self.main_box.pop(0) if self.main_box else ''),
        #
        #     "".join(healthbox.pop(0) if healthbox else ''),
        #     nr=nr
        #     )
        print("This is how it could look.")
        s = ''
        for row in self.main_box:
            s += '\n'
            s += " ".join(row)
        self.add_to_print('room', s, {'horizontal_order': 1, 'width': 40})
        self.add_to_print('stats', healthbox, {'horizontal_order': 2, 'width': 20, 'allignment': '<'})
        self.add_to_print('room2', s, {'horizontal_order': 1, 'width': 40, 'delay': 11})

        self.print_canvas()

    """
        # IDEA: Takes in dictionaries, like so:
        {
            'horizontal_order'  : 1     # Order of who goes first from left to right
            'string'            : 'This is what will get printed and split to lines'
            'delay'             : 0     # if it needs to be x lines below
            'width'             : 30    # how wide will it print
            (optional thoughts)
            'allignment'        : < , > or ^ for the format
            'max_lines'         : 30    # for the string that keeps getting bigger. Take only the latest 30

        }

        it needs some kind of identifier so it is updateable.


    """

c = Canvas().print_example()
