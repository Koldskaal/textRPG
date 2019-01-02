board = []

for x in range(0,6):
    board.append(["X"]*5)
for x in range(1,len(board)-1):


def print_board(board):
    for row in board:
        print(" ".join(row))

print_board(board)
