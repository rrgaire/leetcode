"""
1091. Shortest Path in Binary Matrix
Solved
Medium
Topics
Companies
Hint
Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

All the visited cells of the path are 0.
All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).
The length of a clear path is the number of visited cells of this path.

 

Example 1:


Input: grid = [[0,1],[1,0]]
Output: 2
Example 2:


Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
Output: 4
Example 3:

Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
Output: -1
 

Constraints:

n == grid.length
n == grid[i].length
1 <= n <= 100
grid[i][j] is 0 or 1

"""

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        N = len(grid)
        dirs = [
                [0, 1], [0, -1], [1, 1], [1, -1],
                [1, 0], [-1, 0], [-1, -1], [-1, 1]
            ]

        q = deque()
        visited = set()

        if grid[0][0] == 0 and grid[N - 1][N - 1] == 0:
            q.append((0, 0))
            visited.add((0, 0))

        res = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                if r == c == N - 1:
                    return res + 1
                for dr, dc in dirs:
                    nr = r + dr
                    nc = c + dc

                    if 0 <= nr < N and 0 <= nc < N and (nr, nc) not in visited and grid[nr][nc] == 0:
                        
                        q.append((nr, nc))
                        visited.add((nr, nc))
            res += 1

        return -1
        
        