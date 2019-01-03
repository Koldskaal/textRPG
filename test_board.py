import keyboard

def cls(): print ("\n" * 50)

board = []
cls()
length = 9 #set side length of the square
hight = 9 #set hight of the square
for x in range(0,hight):
    board.append(["X"]*length)
for x in range(1,len(board)-1):
    y = 1
    while y<length-1:
        board[x][y] = " "
        y = y+1


def print_board(board):
    for row in board:
        print(" ".join(row))

xx = int(length/2)
yy = int(hight/2)
def position(board):
    player = board[xx][yy] = "O"
    # cls()
    print_board(board)
position(board)
print_board(board)



running = True

movement = ['a', 's', 'd', 'w']

def move(event):
    global xx, yy
    if event.name in movement:
        if event.name == "w":
            if board[xx-1][yy] == "X":
                pass
            else:
                player = board[xx][yy] = " "
                xx = xx-1
                position(board)
        elif event.name == "s":
            if board[xx+1][yy] == "X":
                pass
            else:
                player = board[xx][yy] = " "
                xx = xx+1
                position(board)
        elif event.name == "a":
            if board[xx][yy-1] == "X":
                pass
            else:
                player = board[xx][yy] = " "
                yy = yy-1
                position(board)
        elif event.name == "d":
            if board[xx][yy+1] == "X":
                pass
            else:
                player = board[xx][yy] = " "
                yy = yy+1
                position(board)
    if event.name == 'q':
        global running
        running = False

keyboard.on_press(move, suppress=True)

print("Press q for exit")
while running:
    pass

position(board)
