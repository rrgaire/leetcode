"""
52. N-Queens II
Solved
Hard
Topics
Companies
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return the number of distinct solutions to the n-queens puzzle.

 

Example 1:


Input: n = 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown.
Example 2:

Input: n = 1
Output: 1
 

Constraints:

1 <= n <= 9



"""

class Solution:
    def totalNQueens(self, n: int) -> int:

        res = 0
        cols = set()
        nd = set()
        pd = set()

        def backtrack(r):
            nonlocal res
            if r == n:
                res += 1
                return
            
            for c in range(n):
                if c in cols or (r + c) in nd or (r - c) in pd:
                    continue
                
                cols.add(c)
                nd.add(r + c)
                pd.add(r - c)

                backtrack(r + 1)

                cols.remove(c)
                nd.remove(r + c)
                pd.remove(r - c)
            
        backtrack(0)
        return res

        