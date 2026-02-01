N = 3
goal = [[1,2,3],[4,5,6],[7,8,0]]

row_move = [0, 0, -1, 1]
col_move = [-1, 1, 0, 0]

def heuristic(board):
    h = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] != 0 and board[i][j] != goal[i][j]:
                h += 1
    return h

def hill_climbing(board, x, y):
    current_h = heuristic(board)

    while True:
        print("Heuristic =", current_h)
        for row in board:
            print(row)
        print()

        best_h = current_h
        best_board = board
        best_x = x
        best_y = y

        for i in range(4):
            new_x = x + row_move[i]
            new_y = y + col_move[i]

            if 0 <= new_x < N and 0 <= new_y < N:
                new_board = [row[:] for row in board]
                new_board[x][y], new_board[new_x][new_y] = \
                new_board[new_x][new_y], new_board[x][y]

                h = heuristic(new_board)
                if h < best_h:
                    best_h = h
                    best_board = new_board
                    best_x = new_x
                    best_y = new_y

        if best_h >= current_h:
            print("Reached Local Maximum / Solution")
            return

        board = best_board
        x = best_x
        y = best_y
        current_h = best_h

start = [[1,2,3],
         [4,0,5],
         [6,7,8]]

hill_climbing(start, 1, 1)
