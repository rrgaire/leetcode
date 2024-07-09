"""
198. House Robber
Solved
Medium
Topics
Companies
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

 

Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 400


"""

class Solution:
    def rob(self, nums: List[int]) -> int:

        # def helper(i):
        #     if i < 0:
        #         return 0
        #     if i in dp:
        #         return dp[i]
        #     dp[i] = max(nums[i] + helper(i-2), helper(i-1))     
        #     return dp[i]

        
        # dp = {}
        # return helper(len(nums) - 1)


        if len(nums) < 2:
            return max(nums)

        first, second = nums[0], nums[1]

        for i in range(2, len(nums)):

            temp = second
            second = max(nums[i] + first, second)    
            first = max(first, temp)
        return max(first, second)   

        # first, second = 0, 0

        # for i in range(len(nums)):
        #     print(first, second)
        #     temp = max(nums[i] + first, second)
        #     first = second
        #     second = temp

        # return second
            