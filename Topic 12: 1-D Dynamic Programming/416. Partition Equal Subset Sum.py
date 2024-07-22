"""
416. Partition Equal Subset Sum
Solved
Medium
Topics
Companies
Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or false otherwise.

 

Example 1:

Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.
 

Constraints:

1 <= nums.length <= 200
1 <= nums[i] <= 100

"""

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # time: O(n.sum(nums)) | space: O(sum(nums))
        if len(nums) < 2 or sum(nums) % 2:
            return False

        target = sum(nums) // 2
        dp = {}

        def backtrack(i, target):
            if sum(nums[i:]) == target:
                return True
            
            if target < 0 or i == len(nums):
                return False

            if target in dp:
                return dp[target]

            
            dp[target] = backtrack(i+1, target - nums[i]) or backtrack(i+1, target)
            return dp[target]
        
        backtrack(0, target)
        return dp[target]

        # time: O(n.sum(nums)) | space: O(sum(nums))
        
        if len(nums) < 2 or sum(nums) % 2:
            return False

        dp = set()
        dp.add(0)
        target = sum(nums) // 2
        for i in range(len(nums)):
            visited = list(dp)
            for item in visited:
                dp.add(item + nums[i])
                if target in dp:
                    return True
        return False

