"""
213. House Robber II
Solved
Medium
Topics
Companies
Hint
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

 

Example 1:

Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.
Example 2:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 3:

Input: nums = [1,2,3]
Output: 3
 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 1000

"""

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # DP Top-Down Approach
        if len(nums) == 1:
            return nums[0]

        def dfs(i, nums):

            if i >= len(nums):
                return 0
            
            if i in cache:
                return cache[i]
            
            cache[i] = max(nums[i] + dfs(i + 2, nums), dfs(i + 1, nums))
            return cache[i]

        cache = {}
        first = dfs(0, nums[:-1])
        cache = {}
        second = dfs(1, nums)
        return max(first, second)

        # DP Bottom-Up
        if len(nums) == 1:
            return nums[0]
        
        def dp(arr):
            a = 0
            b = 0

            for i in range(len(arr)):
                temp = b
                b = max(a + arr[i], b)
                a = temp
            return b
        
        return max(dp(nums[:-1]), dp(nums[1:]))

        # DP Bottom-Up
        
        if len(nums) < 4:
            return max(nums)
        
        def dp(arr):
            a = arr[0]
            b = arr[1]

            for i in range(2, len(arr)):
                temp = b
                b = max(a + arr[i], b)
                a = max(temp, a)
            return b
        
        return max(dp(nums[:-1]), dp(nums[1:]))
        