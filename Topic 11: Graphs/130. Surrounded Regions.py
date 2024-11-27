"""
130. Surrounded Regions
Solved
Medium
Topics
Companies
You are given an m x n matrix board containing letters 'X' and 'O', capture regions that are surrounded:

Connect: A cell is connected to adjacent cells horizontally or vertically.
Region: To form a region connect every 'O' cell.
Surround: The region is surrounded with 'X' cells if you can connect the region with 'X' cells and none of the region cells are on the edge of the board.
A surrounded region is captured by replacing all 'O's with 'X's in the input matrix board.

 

Example 1:

Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]

Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]

Explanation:


In the above diagram, the bottom region is not captured because it is on the edge of the board and cannot be surrounded.

Example 2:

Input: board = [["X"]]

Output: [["X"]]

 

Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 200
board[i][j] is 'X' or 'O'.


"""


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # time: O(mn) | space: O(mn)
        
        nrows = len(board)
        ncols = len(board[0])
        visited = set()

        def dfs(r, c):

            if r < 0 or r == nrows or c < 0 or c == ncols or (r, c) in visited or board[r][c] != 'O':
                return

            board[r][c] = 'T'
            visited.add((r, c))

            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                row = r + dr
                col = c + dc

                dfs(row, col)

        # for c in range(ncols):
        #     if board[0][c] == 'O':
        #         dfs(0, c)
        #     if board[nrows - 1][c] == 'O':
        #         dfs(nrows - 1, c)
        
        # for r in range(nrows):
        #     if board[r][0] == 'O':
        #         dfs(r, 0)
        #     if board[r][ncols - 1] == 'O':
        #         dfs(r, ncols - 1)

        for r in range(nrows):
            for c in range(ncols):
                if board[r][c] == 'O' and (r in [0, nrows - 1] or c in [0, ncols - 1]):
                    dfs(r, c)

        for r in range(nrows):
            for c in range(ncols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
        
        for r in range(nrows):
            for c in range(ncols):
                if board[r][c] == 'T':
                    board[r][c] = 'O'
        


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        nrows = len(board)
        ncols = len(board[0])

        used = set()

        def dfs(r, c):
            if r < 0 or r >= nrows or c < 0 or c >= ncols:
                return False
            
            if (r, c) in used or board[r][c] == 'X':
                return True
            
            used.add((r, c))
            res = True
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr = r + dr
                nc = c + dc

                res = res and dfs(nr, nc)

            return res

        res = set()
        for r in range(nrows):
            for c in range(ncols):
                used = set()
                if (r, c) not in res and board[r][c] == 'O' and dfs(r, c):
                    res.update(used)
        
        for r in range(nrows):
            for c in range(ncols):
                if (r, c) in res:
                    board[r][c] = 'X'
