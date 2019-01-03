import keyboard

running = True

movement = {'a': (-1,0), 's': (0,1), 'd': (1,0), 'w': (0,-1)}

def move(event):
    if event.name in movement:

        print(event.name)
        print(f'Would move with coordinates {movement[event.name]}')

    if event.name == 'q':
        global running
        running = False

keyboard.on_press(move)

print("Press q for exit")
while running:
    pass
