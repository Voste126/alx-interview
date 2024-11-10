#!/usr/bin/python3
import sys

def print_solution(solution):
    """Print a solution in the required format."""
    print([[row, col] for row, col in enumerate(solution)])

def is_safe(board, row, col):
    """Check if it's safe to place a queen at board[row][col]."""
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def solve_nqueens(N, row=0, solution=[]):
    """Recursively solve the N Queens problem."""
    if row == N:
        print_solution(solution)
        return

    for col in range(N):
        if is_safe(solution, row, col):
            solve_nqueens(N, row + 1, solution + [col])

def main():
    """Main entry point of the program."""
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

    solve_nqueens(N)

if __name__ == "__main__":
    main()

