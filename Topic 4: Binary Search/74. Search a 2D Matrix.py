"""
74. Search a 2D Matrix

Medium

You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

 

Example 1:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
Example 2:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-104 <= matrix[i][j], target <= 104

"""

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # time: O(log(mn)) | space: O(1)
        ra, rb = 0, len(matrix) - 1
        ca, cb = 0, len(matrix[0]) - 1

        row = None

        while ra <= rb:
            mid = ra + (rb - ra) // 2
            if matrix[mid][0] > target:
                rb = mid - 1
            elif matrix[mid][cb] < target:
                ra = mid + 1
            else:
                row = mid
                break
                
        if row == None:
            return False

        while ca <= cb:
            mid = ca + (cb - ca) // 2
            if matrix[row][mid] > target:
                cb = mid - 1
            elif matrix[row][mid] < target:
                ca = mid + 1
            else:
                return True