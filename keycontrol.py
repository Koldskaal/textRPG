import keyboard
from data import room

running = True

r = room.Room((10,9))
r2 = room.Room((5,5))
r.print_room()
movement = {'a': (0,-1), 's': (1,0), 'd': (0,1), 'w': (-1,0)}

def move(event):
    global r
    if event.name in movement:
        r.move_player(movement[event.name])
        r.print_room()

    if event.name == 'q':
        global running
        running = False

keyboard.on_press(move, suppress=True)

print("Press q for exit")


while running:
    pass
