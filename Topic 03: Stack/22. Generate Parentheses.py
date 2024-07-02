"""
22. Generate Parentheses
Medium
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
 

Constraints:

1 <= n <= 8
"""

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        # time: O() | space: O()
        res = []
        stack = []

        def backtrack(opn, cls):

            if opn == cls == n:
                res.append(''.join(stack))
                return

            if opn < n:
                stack.append('(')
                backtrack(opn + 1, cls)
                stack.pop()
            
            if cls < opn:
                stack.append(')')
                backtrack(opn, cls + 1)
                stack.pop()

        backtrack(0, 0)
        return res
        
