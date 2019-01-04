from random import randint

WALL_CHAR_UP_DOWN = 'x'
WALL_CHAR_LEFT_RIGHT = 'x'

class Room:
    def __init__(self, size, prev_room_door=''):
        """
        Arguments
        ---------
            size : tuple
                (x, y) The size of the room

            prev_room_door : string
                Previous position of the door that was walked thorugh
                ("left", "right", "up" or "down")
        """
        self.room = self.generate_border(size)

        self.door = {}
        self.print_door(prev_room_door)

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
        self.player_position[0] + coordinates[0]
        == self.door['next'][0]
        and
        self.player_position[1] + coordinates[1]
        == self.door['next'][1]
        ):
            self.change_room()
            #print([self.door['next']])
        else:
            self.room[self.player_position[0]][self.player_position[1]] = ' '
            self.player_position[0] = self.player_position[0] + coordinates[0]
            self.player_position[1] = self.player_position[1] + coordinates[1]
            self.room[self.player_position[0]][self.player_position[1]] = 'P'

    def print_door(self, prev_room_door):
        # to koordinater sat ind dictionariet door med key next.
        # det første er: randint(1, len(self.room[0])-2), betyder random int mellem 1 og max tal på det lodrette koordinat - 1
        # det andet er: len(self.room[1])-1 , er max tal på det vandrette koordinat så helt til højre.
        # Vi kan overveje at gøre så den vælger en random væg at placere døren i. Lige nu er det altid til højre
        # vi har nu gemt koordinaterne på døren "next"
        self.door['next'] = [randint(1, len(self.room[0])-2),len(self.room[1])-1]

        # Her bruger vi de koordinater vi lige har genereret til at skrive døren ind i rummet.
        # Jeg har valgt at lave døren tom i stedet for en | men det kan vi altid ændre igen.
        self.room[self.door['next'][0]][self.door['next'][1]] = " "

        # Hvis vi kom fra en "left" dør, så vil vi lave en "prev" dør på højre side
        if prev_room_door == 'left':
            # max vandret, helt til højre
            horizontal_coord = len(self.room[1])-1
            # random int mellem 1 og en mindre end max lodret
            vertical_coord = randint(1, len(self.room[0])-2)
            # her gemmer  vi det i en "prev" key, så vi kan slå op senere hvilken dør vi går igennem
            self.door['prev'] = [vertical_coord, horizontal_coord]
            # og sætter den ind i rummet
            self.room[self.door['prev'][0]][self.door['prev'][1]] = " "

        elif prev_room_door == 'right':
            # resten er samme princip som den første.
            # døren her kommer fra en dør der lå til højre, så den må ligge til venstre.
            horizontal_coord = 0
            vertical_coord = randint(1, len(self.room[0])-2)
            self.door['prev'] = [vertical_coord, horizontal_coord]
            self.room[self.door['prev'][0]][self.door['prev'][1]] = " "

        elif prev_room_door == 'up':
            # kommer fra op så den må ligge nederst.
            horizontal_coord = randint(1, len(self.room[1])-2)
            vertical_coord = len(self.room[0])-1
            self.door['prev'] = [vertical_coord, horizontal_coord]
            self.room[self.door['prev'][0]][self.door['prev'][1]] = " "

        elif prev_room_door == 'down':
            # kommer fra nede så den må ligge øverst
            horizontal_coord = randint(1, len(self.room[1])-2)
            vertical_coord = 0
            self.door['prev'] = [vertical_coord, horizontal_coord]
            self.room[self.door['prev'][0]][self.door['prev'][1]] = " "

    def change_room(self):
        self.go_to_next = True


if __name__ == '__main__':
    r = Room((9,9), 'up') #tester med et rum der er 25 gange 25
    r.print_room()
