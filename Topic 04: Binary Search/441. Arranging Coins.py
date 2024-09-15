"""
441. Arranging Coins
Solved
Easy
Topics
Companies
You have n coins and you want to build a staircase with these coins. The staircase consists of k rows where the ith row has exactly i coins. The last row of the staircase may be incomplete.

Given the integer n, return the number of complete rows of the staircase you will build.

 

Example 1:


Input: n = 5
Output: 2
Explanation: Because the 3rd row is incomplete, we return 2.
Example 2:


Input: n = 8
Output: 3
Explanation: Because the 4th row is incomplete, we return 3.
 

Constraints:

1 <= n <= 231 - 1


"""

class Solution:
    def arrangeCoins(self, n: int) -> int:
        
        # time: O(sqrt(n)) | space: O(1)
        l = 0
        while n > 0:
            l += 1
            n -= l
        return l if not n else l - 1

        time: O(logn) | space: O(1)

        l = 1
        r = n 
        
        while l <= r:
            m = l + (r - l) // 2
            sums = m * (m + 1) / 2
            if sums < n:
                l = m + 1
            elif sums > n:
                r = m - 1
            else:
                return m
        return l - 1 if l > r else l 