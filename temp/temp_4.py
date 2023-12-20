def is_safe(board, row, col):
    n = len(board)

    # Check if there's a queen in the same row to the left
    for i in range(col):
        if board[row][i]:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j]:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j]:
            return False

    return True

def print_board(board):
    for row in board:
        print(" ".join(map(str, row)))

def solve_queens_util(board, col, solutions):
    n = len(board)
    if col >= n:
        solutions.append([row[:] for row in board])
        return

    for i in range(n):
        if is_safe(board, i, col):
            board[i][col] = 1
            solve_queens_util(board, col + 1, solutions)
            board[i][col] = 0

def solve_queens():
    board = [[0 for _ in range(8)] for _ in range(8)]
    solutions = []
    solve_queens_util(board, 0, solutions)
    return solutions

# Main
solutions = solve_queens()

if solutions:
    print("All Solutions:")
    for idx, solution in enumerate(solutions):
        print(f"Solution {idx}:")
        print_board(solution)
        print()

    print("0th Index Solution:")
    print_board(solutions[0])
else:
    print("No solutions found.")
