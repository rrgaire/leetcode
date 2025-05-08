"""
1137. N-th Tribonacci Number
Solved
Easy
Topics
Companies
Hint
The Tribonacci sequence Tn is defined as follows: 

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.

 

Example 1:

Input: n = 4
Output: 4
Explanation:
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4
Example 2:

Input: n = 25
Output: 1389537
 

Constraints:

0 <= n <= 37
The answer is guaranteed to fit within a 32-bit integer, ie. answer <= 2^31 - 1.

"""
class Solution:
    def tribonacci(self, n: int) -> int:

        # DP Top-Down (Memoization)
        cache = {}

        def dfs(i):
            if i == 0:
                return 0
            if i == 1 or i == 2:
                return 1
            
            if i in cache:
                return cache[i]
            cache[i] = 0
            for j in range(1, 4):
                cache[i] += dfs(i - j)
            return cache[i]
        
        return dfs(n)

        

        # DP Bottom-UP
        dp = [1] * (n + 1)
        dp[0] = 0

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
        
        return dp[n]


        # DP Bottom-UP (Space Optimized)
        a = 0
        b = 1
        c = 1

        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1

        for i in range(3, n + 1):
            t = c
            c = a + b + c
            a = b
            b = t
        
        return c

        dp = [0, 1, 1]

        for i in range(3, n + 1):
            dp[i % 3] = sum(dp)
        
        return dp[n % 3]