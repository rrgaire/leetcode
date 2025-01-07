"""
1020. Number of Enclaves
Solved
Medium
Topics
Companies
Hint
You are given an m x n binary matrix grid, where 0 represents a sea cell and 1 represents a land cell.

A move consists of walking from one land cell to another adjacent (4-directionally) land cell or walking off the boundary of the grid.

Return the number of land cells in grid for which we cannot walk off the boundary of the grid in any number of moves.

 

Example 1:


Input: grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
Output: 3
Explanation: There are three 1s that are enclosed by 0s, and one 1 that is not enclosed because its on the boundary.
Example 2:


Input: grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
Output: 0
Explanation: All 1s are either on the boundary or can reach the boundary.
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 500
grid[i][j] is either 0 or 1.

"""

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:

        nrows = len(grid)
        ncols = len(grid[0])

        # def dfs(r, c):
        #     if r < 0 or r >= nrows or c < 0 or c >= ncols or not grid[r][c]:
        #         return
            
        #     grid[r][c] = 0

        #     for dr, dc in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
        #         nr, nc = r + dr, c + dc
        #         dfs(nr, nc)

        # for r in range(nrows):
        #     if grid[r][0]:
        #         dfs(r, 0)
        #     if grid[r][ncols - 1]:
        #         dfs(r, ncols - 1)
        # for c in range(ncols):
        #     if grid[0][c]:
        #         dfs(0, c)
        #     if grid[nrows - 1]:
        #         dfs(nrows - 1, c)

        # res = 0
        # for r in range(nrows):
        #     for c in range(ncols):
        #         res += grid[r][c]
        
        # return res
                

        def dfs(r, c):
            if r < 0 or r >= nrows or c < 0 or c >= ncols or not grid[r][c] or (r, c) in visit:
                return 0
            
            visit.add((r, c))
            res = 1
            for dr, dc in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                nr, nc = r + dr, c + dc
                res += dfs(nr, nc)
            return res

        enclaves = 0
        visit = set()

        for r in range(nrows):
            for c in range(ncols):
                enclaves += grid[r][c]
                if grid[r][c] and (r, c) not in visit and (r in [0, nrows - 1] or c in [0, ncols - 1]):
                    enclaves -= dfs(r, c)
        return enclaves

        

        
                
        