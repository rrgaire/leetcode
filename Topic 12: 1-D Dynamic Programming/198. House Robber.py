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
        # Soln 1: time: O(n) | space: O(n)

        def backtrack(i):
            if i < 0:
                return 0
            if i in dp:
                return dp[i]
            dp[i] = max(nums[i] + backtrack(i-2), backtrack(i-1))     
            return dp[i]

        
        dp = {}
        return backtrack(len(nums) - 1)

        # Soln 2: time: O(n) | space: O(n)
        
        def backtrack(i):
            if i >= len(nums):
                return 0
            if i in dp:
                return dp[i]

            dp[i] = max(nums[i] + backtrack(i+2), backtrack(i+1))
            return dp[i]

        dp = {}
        return backtrack(0)

        # Soln 3: time: O(n) | space: O(1)

        if len(nums) < 3:
            return max(nums)
 
        first = nums[0]
        second = nums[1]

        for i in range(2, len(nums)):
            temp = second 
            second = max(nums[i] + first, second)
            first = max(first, temp)

        return second

        # Soln 4: time: O(n) | space: O(1)

        if len(nums) < 3:
            return max(nums)
        
        first = 0
        second = 0
        
        for i in range(len(nums)):
            temp = second
            second = max(nums[i] + first, second)
            first = temp
        
        return second