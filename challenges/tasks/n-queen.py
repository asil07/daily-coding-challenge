def solve_n_queens(n):
    def is_valid(board, row, col):
        # Check if there's a queen in the same column or in the diagonal paths
        for i in range(row):
            if board[i] == col or \
               board[i] - i == col - row or \
               board[i] + i == col + row:
                return False
        return True

    def solve(row):
        if row == n:
            # Generate the board configuration from the column placements
            solution = []
            for i in range(n):
                line = ['.'] * n
                line[board[i]] = 'Q'
                solution.append("".join(line))
            results.append(solution)
            return
        
        # Try placing a queen in each column of the current row
        for col in range(n):
            if is_valid(board, row, col):
                board[row] = col
                solve(row + 1)
                board[row] = -1  # Backtrack

    results = []
    board = [-1] * n  # -1 indicates no queen placed in the row
    solve(0)
    return results
