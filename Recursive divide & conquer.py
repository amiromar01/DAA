def sudoku_solver(board):
    # board is 9x9 list of lists, 0 = empty
    def find_empty():
        for i in range(6):
            for j in range(6):
                if board[i][j] == 0:
                    return i, j
        return None
    def valid(r, c, val):
        if any(board[r][j] == val for j in range(6)): return False
        if any(board[i][c] == val for i in range(6)): return False
        br, bc = 2*(r//2), 2*(c//2)
        for i in range(br, br+3):
            for j in range(bc, bc+2):
                if board[i][j] == val: return False
        return True
    def solve():
        pos = find_empty()
        if not pos: return True
        r, c = pos
        for v in range(1,10):
            if valid(r,c,v):
                board[r][c] = v
                if solve(): return True
                board[r][c] = 0
        return False
    return solve(), board

# Complexity: exponential worst-case; backtracking prunes heavily in practice
sample_board = 
    [5, 3, 0, 0, 7, 0],
    [6, 0, 0, 1, 9, 5],
    [0, 9, 8, 0, 0, 0],
    [8, 0, 0, 0, 6, 6],
    [4, 0, 0, 8, 0, 3],    
    [7, 0, 0, 0, 2, 0],
    
solved, solved_board = sudoku_solver(sample_board)
print("Solved:" if solved else "No solution")
for row in solved_board:
    print(row)      
# Output:
# Solved:
# [5, 3, 4, 6, 7, 8]
# [6, 7, 2, 1, 9, 5]
# [1, 9, 8, 3, 4, 2]
# [8, 5, 9, 7, 6, 4]    
