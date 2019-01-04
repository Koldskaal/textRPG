WALL_CHAR_UP_DOWN = 'x'
WALL_CHAR_LEFT_RIGHT = 'x'

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
        self.print_door()

        self.go_to_next = None

    def generate_border(self, size):
        map = []
        x, y = size
        for i_x in range(x):
            row = []
            for i_y in range(y):
                if i_x == 0  or i_x == x - 1:
                    row.append(WALL_CHAR_UP_DOWN)
                elif i_y == 0 or i_y == y - 1:
                    row.append(WALL_CHAR_LEFT_RIGHT)
                else:
                    row.append(' ')
            map.append(row)

        return map

    def spawn_player(self):
            self.room[self.player_position[0]][self.player_position[1]] = 'P'

    def print_room(self):
        for row in self.room:
            print(' '.join(row))

    def move_player(self, coordinates):
        if (
        self.room
        [self.player_position[0] + coordinates[0]]
        [self.player_position[1] + coordinates[1]]
        == "x"
        ):
            pass
        elif (
        self.room
        [self.player_position[0] + coordinates[0]]
        [self.player_position[1] + coordinates[1]]
        == "|"
        ):
            self.change_room()
        else:
            self.room[self.player_position[0]][self.player_position[1]] = ' '
            self.player_position[0] = self.player_position[0] + coordinates[0]
            self.player_position[1] = self.player_position[1] + coordinates[1]
            self.room[self.player_position[0]][self.player_position[1]] = 'P'

    def print_door(self):
        door_coordinates = [int(len(self.room[0])/2),len(self.room[1])-1]
        self.room[door_coordinates[0]][door_coordinates[1]] = "|"

    def change_room(self):
        self.go_to_next = True


if __name__ == '__main__':
    r = Room((9,9)) #tester med et rum der er 25 gange 25

    r.print_room()

    r.move_player((0,1))
    r.print_room()
