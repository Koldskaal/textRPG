import keyboard
from data import room

running = True

r = room.Room((10,9))
r.print_room()
movement = {'a': (-1,0), 's': (0,1), 'd': (1,0), 'w': (0,-1)}

def move(event):
    global r
    if event.name in movement:

        print(event.name)
        print(f'Would move with coordinates {movement[event.name]}')
        r.move_player(movement[event.name])
        r.print_room()

    if event.name == 'q':
        global running
        running = False

keyboard.on_press(move, suppress=True)

print("Press q for exit")


while running:
    pass
