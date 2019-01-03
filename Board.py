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

move_up = (input("Move up: Type w"))
#move_up = w #for testing purpose
if move_up == w:
    player = board[xx][yy] = " "
    xx = xx-1
    def position(board):
        player = board[xx][yy] = "O"
        return xx
        return yy
else:
    pass
move_down = (input("Move up: Type s"))
#move_down = s #for testing purpose
if move_up == s:
    player = board[xx][yy] = " "
    xx = xx+1
    def position(board):
        player = board[xx][yy] = "O"
        return xx
        return yy
else:
    pass
move_left = (input("Move up: Type a"))
#move_let = a #for testing purpose
if move_left == a:
    player = board[xx][yy] = " "
    yy = yy-1
    def position(board):
        player = board[xx][yy] = "O"
        return xx
        return yy
else:
    pass
move_right = (input("Move up: Type d"))
#move_right = d #for testing purpose
if move_up == d:
    player = board[xx][yy] = " "
    yy = yy+1
    def position(board):
        player = board[xx][yy] = "O"
        return xx
        return yy
else:
    pass

position(board)
print_board(board)
