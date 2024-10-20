"""
652. Find Duplicate Subtrees
Solved
Medium
Topics
Companies
Given the root of a binary tree, return all duplicate subtrees.

For each kind of duplicate subtrees, you only need to return the root node of any one of them.

Two trees are duplicate if they have the same structure with the same node values.

 

Example 1:


Input: root = [1,2,3,4,null,2,4,null,null,4]
Output: [[2,4],[4]]
Example 2:


Input: root = [2,1,1]
Output: [[1]]
Example 3:


Input: root = [2,2,2,3,null,3,null]
Output: [[2,3],[3]]
 

Constraints:

The number of the nodes in the tree will be in the range [1, 5000]
-200 <= Node.val <= 200

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:

        res = []
        subtrees = {}

        def dfs(node):
            if not node:
                return 'null'
            
            s = ','.join([str(node.val), dfs(node.left), dfs(node.right)])
            if s not in subtrees:
                subtrees[s] = []
            if len(subtrees[s]) == 1:
                res.append(node)
            subtrees[s].append(node)
            return s
        
        dfs(root)
        return res

        