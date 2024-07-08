"""
70. Climbing Stairs
Solved
Easy
Topics
Companies
Hint
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
 

Constraints:

1 <= n <= 45

"""

class Solution:
    def climbStairs(self, n: int) -> int:

        # # recursive DP | time: O(n) | space: O(n)
        # dp = {}
        # def helper(i):
        #     if i < 0:
        #         return 0
        #     if i == 0:
        #         return 1
        #     if i in dp:
        #         return dp[i]
        #     dp[i] = helper(i-1) + helper(i-2)
        #     return dp[i]
        
        # return helper(n)


        # iterative DP | time: O(n) | space: O(n)
        dp = {}
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]
        
        # # neetcode
        # if n <= 3:
        #     return n
        # n1 = 1
        # n2 = 2

        # for i in range(3, n+1):
        #     n1, n2 = n2, n1 + n2

        # return n2