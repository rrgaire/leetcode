"""
1905. Count Sub Islands
Solved
Medium
Topics
Companies
Hint
You are given two m x n binary matrices grid1 and grid2 containing only 0's (representing water) and 1's (representing land). An island is a group of 1's connected 4-directionally (horizontal or vertical). Any cells outside of the grid are considered water cells.

An island in grid2 is considered a sub-island if there is an island in grid1 that contains all the cells that make up this island in grid2.

Return the number of islands in grid2 that are considered sub-islands.

 

Example 1:


Input: grid1 = [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]], grid2 = [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]
Output: 3
Explanation: In the picture above, the grid on the left is grid1 and the grid on the right is grid2.
The 1s colored red in grid2 are those considered to be part of a sub-island. There are three sub-islands.
Example 2:


Input: grid1 = [[1,0,1,0,1],[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,1],[1,0,1,0,1]], grid2 = [[0,0,0,0,0],[1,1,1,1,1],[0,1,0,1,0],[0,1,0,1,0],[1,0,0,0,1]]
Output: 2 
Explanation: In the picture above, the grid on the left is grid1 and the grid on the right is grid2.
The 1s colored red in grid2 are those considered to be part of a sub-island. There are two sub-islands.
 

Constraints:

m == grid1.length == grid2.length
n == grid1[i].length == grid2[i].length
1 <= m, n <= 500
grid1[i][j] and grid2[i][j] are either 0 or 1.

"""

class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:

        nrows = len(grid1)
        ncols = len(grid1[0])

        def backtrack(r, c):
            if r < 0 or r >= nrows or c < 0 or c >= ncols or grid2[r][c] == 0 or (r, c) in used:
                return True

            

            used.add((r, c))
            res = True

            if grid1[r][c] == 0:
                res = False
            

            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                row = r + dr
                col = c + dc

                res = backtrack(row, col) and res
            
            return res


        res = 0
        used = set()
        for r in range(nrows):
            for c in range(ncols):
                if grid2[r][c] == 1 and (r, c) not in used and backtrack(r, c):
                    res += 1


        return res
        
        


        