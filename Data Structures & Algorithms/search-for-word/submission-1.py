class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def search(grid, row, col, pos):

            if pos == len(word): return True

            for i in [
                (-1, 0),(+1, 0),
                (0, -1),(0, +1)]:
                nr = row + i[0]
                nc = col + i[1]
                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == word[pos]:
                    tl = grid[nr][nc]
                    grid[nr][nc] = "#"
                    if search(grid, nr, nc, pos + 1):
                        return True
                    grid[nr][nc] = tl
            return False
            
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    tl = board[i][j]
                    board[i][j] = "#"
                    if search(board, i, j, 1):
                        return True
                    board[i][j] = tl
        return False
