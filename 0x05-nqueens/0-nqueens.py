import sys

def is_safe(board, row, col):
    # Check the column
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def solve_nqueens(N, board, row, solutions):
    if row == N:
        solutions.append(board[:])
        return

    for col in range(N):
        if is_safe(board, row, col):
            board[row] = col
            solve_nqueens(N, board, row + 1, solutions)
            board[row] = -1

def print_solutions(solutions):
    for solution in solutions:
        formatted_solution = []
        for i in range(len(solution)):
            formatted_solution.append([i, solution[i]])
        print(formatted_solution)

def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)
    
    board = [-1] * N
    solutions = []
    solve_nqueens(N, board, 0, solutions)
    print_solutions(solutions)

if __name__ == "__main__":
    main()
