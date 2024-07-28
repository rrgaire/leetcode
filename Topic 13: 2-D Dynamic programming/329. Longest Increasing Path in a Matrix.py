"""
329. Longest Increasing Path in a Matrix
Solved
Hard
Topics
Companies
Given an m x n integers matrix, return the length of the longest increasing path in matrix.

From each cell, you can either move in four directions: left, right, up, or down. You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).

 

Example 1:


Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
Output: 4
Explanation: The longest increasing path is [1, 2, 6, 9].
Example 2:


Input: matrix = [[3,4,5],[3,2,6],[2,2,1]]
Output: 4
Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
Example 3:

Input: matrix = [[1]]
Output: 1
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 200
0 <= matrix[i][j] <= 231 - 1

"""

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        nrows = len(matrix)
        ncols = len(matrix[0])

        dp = {}

        def backtrack(i, j, prev):

            if i < 0 or i == nrows or j < 0 or j == ncols or matrix[i][j] <= prev:
                return 0

            if (i, j) in dp:
                return dp[(i, j)]

            count = 1

            for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                ni = i + di
                nj = j + dj
                count = max(count, 1 + backtrack(ni, nj, matrix[i][j]))
            dp[(i, j)] = count
            return count

        res = 0
        for i in range(nrows):
            for j in range(ncols):
                    res = max(res, backtrack(i, j, float('-infinity')))
        
        return res 