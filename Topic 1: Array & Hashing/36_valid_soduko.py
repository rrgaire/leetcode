"""
36. Valid Sudoku

Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.


"""

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # time: O(n^2) | space: O(n^2)
        # hashdict = {}
        # nrows = len(board)
        # ncols = len(board[0])

        # for row in range(nrows):
        #     hashset = set()
        #     for col in range(ncols):
        #         num = board[row][col]
        #         if num != '.':
        #             if num not in hashset:
        #                 hashset.add(num)
        #             else:
        #                 return False
        
        # for col in range(ncols):
        #     hashset = set()
        #     for row in range(nrows):
        #         num = board[row][col]
        #         if num != '.':
        #             if num not in hashset:
        #                 hashset.add(num)
        #             else:
        #                 return False


        # for row in range(0, nrows, 3):
        #     for col in range(0, ncols, 3):
        #         hashset = set()
        #         for i in range(row, row+3):
        #             for k in range(col, col+3):
        #                 print(row+i, col+k)
        #                 num = board[i][k]
        #                 if num != '.':
        #                     if num not in hashset:
        #                         hashset.add(num)
        #                     else:
        #                         return False
        # return True


        # time: O(n^2) | space: O(n^2)

        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for row in range(len(board)):
            for col in range(len(board[0])):
                num = board[row][col]

                if num != '.':
                    if num in rows[row] or num in cols[col] or num in squares[(row//3, col//3)]:
                        return False
                    rows[row].add(num)
                    cols[col].add(num)
                    squares[(row//3, col//3)].add(num)
        return True