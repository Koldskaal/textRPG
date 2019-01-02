import numpy

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
        for i in range(x):
            small = []
            for o in range(y):
                if o == 0 or o == y - 1 or i == 0  or i == x - 1:
                    small.append('x')
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
