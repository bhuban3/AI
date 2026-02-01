import heapq

N = 3

class Board:
    def __init__(self, board, x, y, depth):
        self.board = board
        self.x = x
        self.y = y
        self.depth = depth
        self.h = heuristic_value(board)
        self.f = self.depth + self.h

    def __lt__(self, other):
        return self.f < other.f


row = [0, 0, -1, 1]
column = [-1, 1, 0, 0]

GOAL_STATE = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]


def is_valid(x, y):
    return 0 <= x < N and 0 <= y < N


def is_goal(board):
    return board == GOAL_STATE


def heuristic_value(board):
    distance = 0
    for i in range(N):
        for j in range(N):
            val = board[i][j]
            if val != 0:
                for k in range(N):
                    for l in range(N):
                        if GOAL_STATE[k][l] == val:
                            distance += abs(i - k) + abs(j - l)
    return distance


def a_star_search(start, x, y):
    pq = []
    visited = set()

    start_node = Board(start, x, y, 0)
    heapq.heappush(pq, start_node)

    while pq:
        current = heapq.heappop(pq)

        board_tuple = tuple(map(tuple, current.board))
        if board_tuple in visited:
            continue

        visited.add(board_tuple)

        print("Depth:", current.depth)
        for r in current.board:
            print(r)
        print()

        if is_goal(current.board):
            print("Solution found at depth:", current.depth)
            return

        for i in range(4):
            new_x = current.x + row[i]
            new_y = current.y + column[i]

            if is_valid(new_x, new_y):
                new_board = [r[:] for r in current.board]

                new_board[current.x][current.y], new_board[new_x][new_y] = (
                    new_board[new_x][new_y],
                    new_board[current.x][current.y],
                )

                if tuple(map(tuple, new_board)) not in visited:
                    next_node = Board(
                        new_board, new_x, new_y, current.depth + 1
                    )
                    heapq.heappush(pq, next_node)

    print("No solution found.")


start_board = [
    [1, 4, 6],
    [0, 8, 2],
    [3, 7, 5]
]

x, y = 1, 0
a_star_search(start_board, x, y)  
