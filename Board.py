board = []

length = 7 #set side length of the square
for x in range(0,length):
    board.append(["X"]*length)
for x in range(1,len(board)-1):
    y = 1
    while y<length-1:
        board[x][y] = " "
        y = y+1


def print_board(board):
    for row in board:
        print(" ".join(row))

print_board(board)
