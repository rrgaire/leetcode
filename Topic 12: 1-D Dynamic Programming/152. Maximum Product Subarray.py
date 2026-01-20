"""
152. Maximum Product Subarray
Solved
Medium
Topics
Companies
Given an integer array nums, find a 
subarray
 that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

 

Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
 

Constraints:

1 <= nums.length <= 2 * 104
-10 <= nums[i] <= 10
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.


"""

class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        # Brute Force: O(n ^ 2) | O(1)
        res = float('-inf')

        for i in range(len(nums)):
            res = max(res, nums[i])
            prod = nums[i]
            for j in range(i + 1, len(nums)):
                prod *= nums[j]
                res = max(res, prod)
        return res

        # Dynamic Programming: O(n ^ 2) | O(1)
        curMax = 1
        curMin = 1
        res = nums[0]

        for i in range(len(nums)):
            tmp = curMax * nums[i]
            curMax = max(tmp, curMin * nums[i], nums[i])
            curMin = min(tmp, curMin * nums[i], nums[i])
            res = max(res, curMax)
        return res
