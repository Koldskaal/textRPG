board = []

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
    return xx
    return yy
position(board)
print_board(board)
print("Movement: W A S D")
movement = input()
if movement == "w":
    player = board[xx][yy] = " "
    xx = xx-1
    position(board)
elif movement == "s":
        player = board[xx][yy] = " "
        xx = xx+1
        position(board)
elif movement == "a":
        player = board[xx][yy] = " "
        yy = yy-1
        position(board)
elif movement == "d":
        player = board[xx][yy] = " "
        yy = yy+1
        position(board)
else:
    print("invalid key")
position(board)
print_board(board)
