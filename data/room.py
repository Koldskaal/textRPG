WALL_CHAR_UP_DOWN = '+'
WALL_CHAR_LEFT_RIGHT = '+'

class Room:
    def __init__(self, size):
        """
        Arguments
        ---------
            size : tuple
                (x, y) The size of the room
        """
        self.room = self.generate_border(size)
        self.has_been_entered_before = False

    def generate_border(self, size):
        map = []
        x, y = size
        for i_x in range(x):
            small = []
            for i_y in range(y):
                if i_x == 0  or i_x == x - 1:
                    small.append(WALL_CHAR_UP_DOWN)
                elif i_y == 0 or i_y == y - 1:
                    small.append(WALL_CHAR_LEFT_RIGHT)
                else:
                    small.append(' ')
            map.append(small)

        return map

    def print_room(self):
        for row in self.room:
            print(' '.join(row))


if __name__ == '__main__':
    r = Room((25,25)) #tester med et rum der er 25 gange 25
    r.print_room()
