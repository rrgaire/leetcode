"""
1254. Number of Closed Islands
Solved
Medium
Topics
Companies
Hint
Given a 2D grid consists of 0s (land) and 1s (water).  An island is a maximal 4-directionally connected group of 0s and a closed island is an island totally (all left, top, right, bottom) surrounded by 1s.

Return the number of closed islands.

 

Example 1:



Input: grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
Output: 2
Explanation: 
Islands in gray are closed because they are completely surrounded by water (group of 1s).
Example 2:



Input: grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
Output: 1
Example 3:

Input: grid = [[1,1,1,1,1,1,1],
               [1,0,0,0,0,0,1],
               [1,0,1,1,1,0,1],
               [1,0,1,0,1,0,1],
               [1,0,1,1,1,0,1],
               [1,0,0,0,0,0,1],
               [1,1,1,1,1,1,1]]
Output: 2
 

Constraints:

1 <= grid.length, grid[0].length <= 100
0 <= grid[i][j] <=1

"""

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:

        nrows = len(grid)
        ncols = len(grid[0])

        visited = set()

        # def dfs(r, c):
        #     nonlocal accept
        #     if r < 0 or r >= nrows or c < 0 or c >= ncols:
        #         accept = False
        #         return
            
        #     if grid[r][c] == 1 or (r, c) in visited:
        #         return
            
        #     visited.add((r, c))

        #     for dr, dc in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
        #         nr = r + dr
        #         nc = c + dc

        #         dfs(nr, nc)

        # res = 0
        # for r in range(1, nrows - 1):
        #     for c in range(1, ncols - 1):
        #         if grid[r][c] == 0 and (r, c) not in visited:
        #             accept = True
        #             dfs(r, c)
        #             if accept:
        #                 res += 1
        
        def dfs(r, c):
            if (r == 0 or r == nrows - 1 or c == 0 or c == ncols - 1) and not grid[r][c]:
                return False
            
            if grid[r][c] == 1 or (r, c) in visited:
                return True

            visited.add((r, c))

            res = True
            for dr, dc in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                nr = r + dr
                nc = c + dc
                res = min(res, int(dfs(nr, nc)))
            return res

        res = 0
        for r in range(nrows):
            for c in range(ncols):
                if grid[r][c] == 0 and (r, c) not in visited and dfs(r, c):
                    res += 1

        return res
                    
        