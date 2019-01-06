import msvcrt
import keyboard
from data import room, room_controller
import sys


running = True

#other = room.Room((15,15))
r = room_controller.RoomController(room.Room((10,9), room_nr='0'))
#r.assign_next_room(other)

r.print_room()
movement = {'a': (0,-1), 's': (1,0), 'd': (0,1), 'w': (-1,0)}



print("Press q for exit")

if sys.stdin.isatty():
    while running:
        if msvcrt.kbhit():
            key = ord(msvcrt.getch())
            if chr(key) in movement:
                print('\n'*20)
                r.move_player(movement[chr(key)])
                r.print_room()

            if key == ord('q'):
                running = False
else:
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

    while running:
        pass
