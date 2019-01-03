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

#move_up = (raw_input("Move up: Type w"))
move_up = 1
if move_up == 1:
    player = board[xx][yy] = " "
    xx = xx-1
    def position(board):
        player = board[xx][yy] = "I"
        return xx
        return yy
else:
    pass
position(board)
print_board(board)
