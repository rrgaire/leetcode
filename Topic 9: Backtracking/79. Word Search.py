"""
79. Word Search
Solved
Medium
Topics
Companies
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

 

Example 1:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
Example 2:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true
Example 3:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
 

Constraints:

m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board and word consists of only lowercase and uppercase English letters.
 

"""

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # time: O(m.n.4^n)
        nrows = len(board)
        ncols = len(board[0])

        path = set()

        def backtrack(r, c, i):
            if i == len(word):
                return True
            if (r < 0 or c < 0 or r >= len(board) or c >= len(board[0]) or word[i] != board[r][c] or (r, c) in path):
                return False
            
            path.add((r, c))
            res = (backtrack(r+1, c, i+1) or
                    backtrack(r-1, c, i+1) or
                    backtrack(r, c+1, i+1) or
                    backtrack(r, c-1, i+1))
            path.remove((r, c))
            return res
            
        # To prevent TLE,reverse the word if frequency of the first letter is more than the last letter's
        count = defaultdict(int, sum(map(Counter, board), Counter()))
        if count[word[0]] > count[word[-1]]:
            word = word[::-1] 


        for r in range(nrows):
            for c in range(ncols):
                if backtrack(r, c, 0):
                    return True
        return False
        