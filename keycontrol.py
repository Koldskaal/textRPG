import keyboard
from data import room, room_controller

running = True

#other = room.Room((15,15))
r = room_controller.RoomController(room.Room((10,9), room_nr='0'))
#r.assign_next_room(other)

r.print_room()
movement = {'a': (0,-1), 's': (1,0), 'd': (0,1), 'w': (-1,0)}

def move(event):
    global r
    if event.name in movement:
        print('\n'*20)
        r.move_player(movement[event.name])
        r.print_room()

    if event.name == 'q':
        global running
        running = False

keyboard.on_press(move, suppress=True)

print("Press q for exit")


while running:
    pass
