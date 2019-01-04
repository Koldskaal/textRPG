from .room import Room

class RoomController:
    def __init__(self, starter_room):
        """
        Arguments
        ---------
            starter_room : class Room
                An instance of a Room()
        """
        self.current_room = starter_room
        self.next_room = None
        self.prev_room = None

    def assign_next_room(self, room):
        self.next_room = room

    def change_room(self):
        self.prev_room = self.current_room
        self.current_room = self.next_room
        self.next_room = None


    def print_room(self):
        self.current_room.print_room()

    def move_player(self, coordinates):
        self.current_room.move_player(coordinates)
        if self.current_room.go_to_next == True:
            self.change_room()
            self.print_room()
