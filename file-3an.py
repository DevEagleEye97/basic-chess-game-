board = []
for i in range(8, 0, -1):
    row = str(i) + " ".join([str(i) + str(j) for j in range(8)])
    board.append(row)

board.append(" a b c d e f g h")