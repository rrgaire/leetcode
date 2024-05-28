"""
15. 3Sum

Medium
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
 

Constraints:

3 <= nums.length <= 3000
-105 <= nums[i] <= 105

"""

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        # time: O(n^2) | space: O(1)
        soln = []
        sorted_nums = sorted(nums)

        for i in range(len(sorted_nums)):
            if i > 0 and sorted_nums[i] == sorted_nums[i-1]:
                continue
            j = i + 1
            k = len(sorted_nums) - 1

            while j < k:
                if sorted_nums[j] + sorted_nums[k] + sorted_nums[i] < 0:
                    j += 1
                elif sorted_nums[j] + sorted_nums[k] + sorted_nums[i] > 0:
                    k -= 1
                else:
                    soln.append([sorted_nums[i], sorted_nums[j], sorted_nums[k]])
                    j += 1

                    while j < k and sorted_nums[j] == sorted_nums[j-1]:
                        j += 1

        return soln      