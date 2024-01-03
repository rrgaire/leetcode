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
        
        
        # for i in range(9):
        #     hash = set()
        #     for j in range(9):
        #         if board[i][j] != '.':
        #             if board[i][j] in hash:
        #                 return False
        #             else:
        #                 hash.update(board[i][j])

        
        # for i in range(9):
        #     hash = set()
        #     for j in range(9):
        #         if board[j][i] != '.':
        #             if board[j][i] in hash:
        #                 return False
        #             else:
        #                 hash.update(board[j][i])


        # for k in range(0, 9, 3):
        #     for l in range(0, 9, 3):
        #         hash = set()
        #         for i in range(k, k + 3):
        #             for j in range(l, l + 3):
        #                 if board[i][j] != '.':
        #                     if board[i][j] in hash:
        #                         return False
        #                     else:
        #                         hash.update(board[i][j])

        # return True


        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        sqrs = collections.defaultdict(set)

        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    if (board[i][j] in rows[i]) or (board[i][j] in cols[j]) or (board[i][j] in sqrs[(i//3, j//3)]):
                        return False
                    else:
                        rows[i].add(board[i][j]) 
                        cols[j].add(board[i][j])
                        sqrs[(i//3, j//3)].add(board[i][j])

        return True