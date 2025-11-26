def solve_n_queens(n):
    cols = set()
    diag1 = set()
    diag2 = set()
    board = [['.']*n for _ in range(n)]
    solutions = []

    def backtrack(r):
        if r == n:
            solutions.append([''.join(row) for row in board])
            return

        for c in range(n):
            if c in cols or (r-c) in diag1 or (r+c) in diag2:
                continue

            cols.add(c)
            diag1.add(r-c)
            diag2.add(r+c)
            board[r][c] = 'Q'

            backtrack(r+1)

            board[r][c] = '.'
            cols.remove(c)
            diag1.remove(r-c)
            diag2.remove(r+c)

    backtrack(0)
    return solutions
print(solve_n_queens(4))
#output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]                   