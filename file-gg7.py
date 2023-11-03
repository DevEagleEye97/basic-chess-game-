initial_board = []
for i in range(8, 0, -1):
    row = str(i) + " ".join([" "] * 8)
    initial_board.append(row)

initial_board.append(" a b c d e f g h")