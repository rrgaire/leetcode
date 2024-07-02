"""
110. Balanced Binary Tree
Solved
Easy
Topics
Companies
Given a binary tree, determine if it is 
height-balanced
.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: true
Example 2:


Input: root = [1,2,2,3,3,null,null,4,4]
Output: false
Example 3:

Input: root = []
Output: true
 

Constraints:

The number of nodes in the tree is in the range [0, 5000].
-104 <= Node.val <= 104

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        # time: O(n) | space: O(n)
        bal = True

        def dfs(node):
            nonlocal bal
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)
            if abs(right - left) > 1:
                bal = False
            return 1 + max(left, right) 
        
        dfs(root)
        return bal