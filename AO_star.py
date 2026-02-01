N = 3
goal = [[1,2,3],[4,5,6],[7,8,0]]

row_move = [0, 0, -1, 1]
col_move = [-1, 1, 0, 0]

def heuristic(board):
    count = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] != 0 and board[i][j] != goal[i][j]:
                count += 1
    return count

def ao_star(board, x, y, depth):
    print("Current State (depth =", depth, ")")
    for row in board:
        print(row)
    print()

    if board == goal:
        print("Goal Reached")
        return

    best_cost = 999
    best_state = None
    best_x = x
    best_y = y

    for i in range(4):
        new_x = x + row_move[i]
        new_y = y + col_move[i]

        if 0 <= new_x < N and 0 <= new_y < N:
            new_board = [row[:] for row in board]
            new_board[x][y], new_board[new_x][new_y] = \
            new_board[new_x][new_y], new_board[x][y]

            cost = 1 + heuristic(new_board)

            if cost < best_cost:
                best_cost = cost
                best_state = new_board
                best_x = new_x
                best_y = new_y

    if best_state:
        ao_star(best_state, best_x, best_y, depth + 1)

start = [[1,2,3],
         [4,0,5],
         [6,7,8]]

ao_star(start, 1, 1, 0)
