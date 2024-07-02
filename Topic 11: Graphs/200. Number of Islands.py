"""
200. Number of Islands
Solved
Medium
Topics
Companies
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.

"""

# Iterative BFS
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        nrows = len(grid)
        ncols = len(grid[0])
        visited = set()
        island = 0

        def bfs(r, c):
            q = deque()
            q.append((r, c))
            visited.add((r, c))

            while q:
                row, col = q.popleft()
                
                for (dr, dc) in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    r = row + dr
                    c = col + dc
                    if r in range(nrows) and c in range(ncols) and (r, c) not in visited and grid[r][c] == '1':
                        q.append((r, c))
                        visited.add((r, c))


        for r in range(nrows):
            for c in range(ncols):
                if (r, c) not in visited and grid[r][c] == '1':
                    bfs(r, c)
                    island += 1

        return island        

# Iterative DFS
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        nrows = len(grid)
        ncols = len(grid[0])
        visited = set()
        island = 0

        def dfs(r, c):
            q = []
            q.append((r, c))
            visited.add((r, c))

            while q:
                row, col = q.pop()
                
                for (dr, dc) in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    r = row + dr
                    c = col + dc
                    if r in range(nrows) and c in range(ncols) and (r, c) not in visited and grid[r][c] == '1':
                        q.append((r, c))
                        visited.add((r, c))


        for r in range(nrows):
            for c in range(ncols):
                if (r, c) not in visited and grid[r][c] == '1':
                    dfs(r, c)
                    island += 1

        return island           

# Recursive DFS
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        nrows = len(grid)
        ncols = len(grid[0])
        visited = set()
        island = 0

        def dfs(r, c):

            if r not in range(nrows) or c not in range(ncols) or (r, c) in visited or grid[r][c] == '0':
                return
            
            visited.add((r, c))

            for (dr, dc) in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                row = r + dr
                col = c + dc
                dfs(row, col)


        for r in range(nrows):
            for c in range(ncols):
                if (r, c) not in visited and grid[r][c] == '1':
                    dfs(r, c)
                    island += 1

        return island  
        