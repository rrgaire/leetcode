"""
934. Shortest Bridge
Solved
Medium
Topics
Companies
You are given an n x n binary matrix grid where 1 represents land and 0 represents water.

An island is a 4-directionally connected group of 1's not connected to any other 1's. There are exactly two islands in grid.

You may change 0's to 1's to connect the two islands to form one island.

Return the smallest number of 0's you must flip to connect the two islands.

 

Example 1:

Input: grid = [[0,1],[1,0]]
Output: 1
Example 2:

Input: grid = [[0,1,0],[0,0,0],[0,0,1]]
Output: 2
Example 3:

Input: grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
Output: 1
 

Constraints:

n == grid.length == grid[i].length
2 <= n <= 100
grid[i][j] is either 0 or 1.
There are exactly two islands in grid.

"""

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:

        nrows = len(grid)
        ncols = len(grid[0])
        visited = set()

        def dfs(r, c):
            if r < 0 or r >= nrows or c < 0 or c >= ncols or grid[r][c] == 0 or (r, c) in visited:
                return
            
            visited.add((r, c))

            for dr, dc in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
                nr = r + dr
                nc = c + dc

                dfs(nr, nc)
        
        def bfs():

            q = deque()
            level = 0

            for pos in visited:
                q.append(pos)

            while q:
                for _ in range(len(q)):
                    r, c = q.popleft()

                    for dr, dc in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
                        nr = r + dr
                        nc = c + dc

                        if nr < 0 or nr >= nrows or nc < 0 or nc >= ncols or (nr, nc) in visited:
                            continue
                        
                        if grid[nr][nc] == 1:
                            return level
                        
                        q.append((nr, nc))
                        visited.add((nr, nc))
                
                level += 1
            return level


        for r in range(nrows):
            for c in range(ncols):
                if grid[r][c] == 1:
                    dfs(r, c)
                    return bfs()
                    
        
       