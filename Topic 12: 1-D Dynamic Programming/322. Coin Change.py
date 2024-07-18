"""
322. Coin Change
Solved
Medium
Topics
Companies
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

 

Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Example 3:

Input: coins = [1], amount = 0
Output: 0
 

Constraints:

1 <= coins.length <= 12
1 <= coins[i] <= 231 - 1
0 <= amount <= 104

"""

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # time: O(n) | space: O(n)
        if amount == 0:
            return 0

        dp = {}

        def backtrack(i):
            if i == 0:
                return 0
            if i < 0:
                return float('infinity')

            if i in dp:
                return dp[i]

            res = float('infinity')
            for c in coins:
                res = min(res, 1 + backtrack(i - c))

            dp[i] = res
            return dp[i]

        backtrack(amount)
        return dp[amount] if dp[amount] != float('infinity') else -1

        # time: O(n) | space: O(1)
        dp = {i: amount + 1 for i in range(amount+1)} 
        dp[0] = 0

        for i in range(1, amount+1):
            count = amount + 1
            for c in coins:
                if i-c >= 0:
                    count = min(count, 1 + dp[i-c])
            dp[i] = count

        return dp[amount] if dp[amount] != amount+1 else -1
