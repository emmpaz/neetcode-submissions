class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def search(grid, row, col, word, current):

            if current == len(word):
                return True
            
            for i in [
                (0,1),
                (0,-1),
                (1,0),
                (-1,0)
            ]:
                    if  0 <= row + i[0] < len(grid) and 0 <= col + i[1] < len(grid[0]) and grid[row + i[0]][col + i[1]] == word[current]:
                        temp = grid[row + i[0]][col + i[1]]
                        grid[row + i[0]][col + i[1]] = "#"
                        if search(grid, row+i[0], col+i[1], word, current+1):
                            grid[row + i[0]][col + i[1]] = temp
                            return True
                        grid[row + i[0]][col + i[1]] = temp
                        
            return False
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    temp = board[i][j]
                    board[i][j] = "#"
                    if search(board, i, j, word, 1):
                        board[i][j] = temp
                        return True
                    board[i][j] = temp
        
        return False
