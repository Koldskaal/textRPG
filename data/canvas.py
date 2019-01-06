""" This scrpit is supposed to tie all objects together to a single print """

class Canvas:
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
        healthbox = """------------------|
 Health: 100/100  |
 Mana:   100/100  |
 Str:    10       |
 Int:    10       |
 Agi:    10       |
------------------|
        """.splitlines()


        lines = max(len(self.main_box), len(healthbox))
        nr = 20
        for i in range(lines):
            string += "\n" + '{: <{nr}}|{: <30}'.format(

            " ".join(self.main_box.pop(0) if self.main_box else ''),

            "".join(healthbox.pop(0) if healthbox else ''),
            nr=nr
            )
        print("This is how it could look.")
        print (string)

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
