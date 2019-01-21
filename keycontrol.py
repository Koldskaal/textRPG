import msvcrt
import keyboard
from data import room, room_controller
import sys

if sys.stdin.isatty():
    import colorama
    import win_unicode_console

    win_unicode_console.enable()
    colorama.init(strip=True)

import cursor
cursor.hide() ## Hides the cursor

running = True

#other = room.Room((15,15))
r = room_controller.RoomController()
#r.assign_next_room(other)
print("Press q for exit.")
r.print_room(True)

movement = {'a': (0,-1), 's': (1,0), 'd': (0,1), 'w': (-1,0), '\r': (0,0)}

if sys.stdin.isatty():
    while running:
        if msvcrt.kbhit():

            key = ord(msvcrt.getch())
                # Pontential flicker killers
                # print("\033[11A\033[J")  # moves curser 11 up then deletes down
                # print("\033[H\033[J")  # moves curser to start corner then deletes down
                # print('\n'*20)

            if key == 224:
                key = ord(msvcrt.getch())
                r.scroll_log(key)
                pass

            if key == 27:
                running = False

            r.use_key(chr(key))
            while msvcrt.kbhit():
                msvcrt.getch()
        if isinstance(r.current_room, room.Room):
            r.current_room.move_monsters()
else:
    def move(event):
        global r
        print(event.name)
        if event.name in movement:
            print('\n'*20)
            r.use_key(event.name)
            r.print_room()

        if event.name == 'q':
            global running
            running = False

    keyboard.on_press(move, suppress=True)

    while running:
        pass

cursor.show()
