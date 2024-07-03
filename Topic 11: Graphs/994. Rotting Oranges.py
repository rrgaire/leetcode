"""
994. Rotting Oranges
Solved
Medium
Topics
Companies
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

 

Example 1:


Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Example 2:

Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
Example 3:

Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 10
grid[i][j] is 0, 1, or 2.

"""

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        nrows = len(grid)
        ncols = len(grid[0])

        nfresh = 0
        visited = set()
        q = deque()

        for r in range(nrows):
            for c in range(ncols):
                if grid[r][c] == 2:
                    q.append((r, c))
                    visited.add((r, c))
                if grid[r][c] == 1:
                    nfresh += 1
        
        time = 0

        while q and nfresh:
            for _ in range(len(q)):
                r, c = q.popleft()

                grid[r][c] = 2

                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    row = r + dr
                    col = c + dc

                    if 0 <= row < nrows and 0 <= col < ncols and (row, col) not in visited and grid[row][col] == 1:
                        nfresh -= 1
                        q.append((row, col))
                        visited.add((row, col))
                
                    
            
            time += 1 #if q else 0

        return time if not nfresh else -1

        