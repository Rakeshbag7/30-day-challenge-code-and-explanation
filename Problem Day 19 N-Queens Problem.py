# Using backtracking

# Check if it's safe to place a queen at position (row, col) on the chessboard
def issafe(board, row, col, n):
    # Check horizontal (same row)
    for j in range(n):
        if board[row][j] == 1:
            return False

    # Check vertical (same column)
    for i in range(n):
        if board[i][col] == 1:
            return False

    # Check left diagonal (top-left direction)
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check right diagonal (top-right direction)
    i, j = row, col
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    # If no conflicts found, it's safe
    return True

# Find all valid ways to place n queens on an n × n chessboard so none attack each other.
def nqueens(board, row, n):
    # If all queens are placed
    if row == n:
        for r in board:
            print(" ".join(str(x) for x in r))
        return True

    # Try placing queen in each column of this row
    for col in range(n):
        if issafe(board, row, col, n):
            board[row][col] = 1  # Place queen

            if nqueens(board, row + 1, n):
                return True  # Stop after first valid solution

            board[row][col] = 0  # Backtrack

    return False


# Main function
n = int(input().strip())

if n < 1 or n > 10:
    print(-1)
else:
    # Initialize an empty board
    board = []
    for y in range(n):
        row = []
        for z in range(n):
            row.append(0)
        board.append(row) # Print the result

    if not nqueens(board, 0, n):
        print(-1)  # Print the result
