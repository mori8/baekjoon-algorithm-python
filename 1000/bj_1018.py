import sys


def compare_board(board, x, y):
    whiteBoard = [
        'WBWBWBWB',
        'BWBWBWBW',
        'WBWBWBWB',
        'BWBWBWBW',
        'WBWBWBWB',
        'BWBWBWBW',
        'WBWBWBWB',
        'BWBWBWBW'
    ]
    blackBoard = [
        'BWBWBWBW',
        'WBWBWBWB',
        'BWBWBWBW',
        'WBWBWBWB',
        'BWBWBWBW',
        'WBWBWBWB',
        'BWBWBWBW',
        'WBWBWBWB'
    ]
    count_white = count_black = 0
    for i in range(8):
        for j in range(8):
            if board[x-7+i][y-7+j] != whiteBoard[i][j]:
                count_white += 1
    for i in range(8):
        for j in range(8):
            if board[x-7+i][y-7+j] != blackBoard[i][j]:
                count_black += 1

    return min([count_white, count_black])


n, m = map(int, input().split())
new_board = []
for line in sys.stdin:
    new_board.append(line.rstrip())
min_list = []
for i in range(7, n):
    for j in range(7, m):
        min_list.append(compare_board(new_board, i, j))
print(min(min_list))
