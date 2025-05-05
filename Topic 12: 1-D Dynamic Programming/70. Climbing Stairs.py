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
        # Dynamic Programming Top-Down (memoization)
        cache = {}

        def dfs(i):
            if i < 0:
                return 0
            if i == 0:
                return 1
            if i in cache:
                return cache[i]
            
            cache[i] = 0
            for di in [1, 2]:
                cache[i] += dfs(i - di)
            return cache[i]
        
        return dfs(n)

        # Dynamic Programming Bottom-Up 
        dp = [1] * (n + 1)

        for i in range(2, n + 1):
            dp[i] = dp[i - 2] + dp[i - 1]
        
        return dp[n]        

        # Dymaic Programming with Constant Memory

        a = 1
        b = 1

        for i in range(2, n + 1):
            t = b
            b = a + b
            a = t
        return b



        

class Solution:
    def climbStairs(self, n: int) -> int:

        # Recursion
        def dfs(i):
            if i == n:
                return 1
            if i > n:
                return 0
            
            res = 0
            for di in [1, 2]:
                res += dfs(i + di)
            return res
        
        return dfs(0)
        
        # Memoiazation

        cache = {}
        def dfs(i):
            if i == n:
                return 1
            
            if i > n:
                return 0

            if i in cache:
                return cache[i]
            
            cache[i] = 0
            for di in [1, 2]:
                cache[i] += dfs(i + di)
            
            return cache[i]
        
        return dfs(0)

        # DP with O(n) memory

        dp = [1] * (n + 1)

        for i in range(n - 2, -1, -1):
            dp[i] = dp[i + 1] + dp[i + 2]
        
        return dp[0]

        # DP with O(1) memory

        a = 1
        b = 1

        for i in range(n-2, -1, -1):
            t = b
            b = a
            a = t + a
        return a
