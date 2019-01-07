import msvcrt
import keyboard
from data import room, room_controller
import sys
from shutil import get_terminal_size
terminal_size = get_terminal_size()
print(terminal_size)
import cursor
cursor.hide() ## Hides the cursor

running = True

#other = room.Room((15,15))
r = room_controller.RoomController(room.Room((10,9), room_nr='0'))
#r.assign_next_room(other)
print("Press q for exit.")
r.print_room()
movement = {'a': (0,-1), 's': (1,0), 'd': (0,1), 'w': (-1,0)}





if sys.stdin.isatty():
    while running:
        if msvcrt.kbhit():
            key = ord(msvcrt.getch())
            if chr(key) in movement:
                # Pontential flicker killers
                # print("\033[11A\033[J")  # moves curser 11 up then deletes down
                print("\033[H\033[J")  # moves curser to start corner then deletes down
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

cursor.show()
