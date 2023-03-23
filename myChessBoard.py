# Creating a chess board
#
# board = []
#
# for m in range(8):
#     board.append(m)
#     for n in range(8):
#         # pass
#         board.append(n)
#
# board[0][0] = "Rook"
# board[0][7] = "Rook"
# board[7][0] = "Rook"
# board[7][7] = "Rook"
#
# print(board)
# print(len(board))

temps = [[0.0 for h in range(24)] for d in range(31)]

print(temps)

total = 0.0

for day in temps:
    total += day[11]

average = total / 31

print("Average temperature at noon:", average)
