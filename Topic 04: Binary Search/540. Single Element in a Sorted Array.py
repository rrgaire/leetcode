"""
540. Single Element in a Sorted Array
Solved
Medium
Topics
Companies
You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.

Return the single element that appears only once.

Your solution must run in O(log n) time and O(1) space.

 

Example 1:

Input: nums = [1,1,2,3,3,4,4,8,8]
Output: 2
Example 2:

Input: nums = [3,3,7,7,10,11,11]
Output: 10
 

Constraints:

1 <= nums.length <= 105
0 <= nums[i] <= 105

"""

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[0]

        l = 0
        r = len(nums) - 1

        while l < r:
            
            m = l + (r - l) // 2
            if nums[m - 1] != nums[m] != nums[m + 1]:
                return nums[m]

            if nums[m] == nums[m + 1]:
                if m % 2:
                    r = m - 1
                else:
                    l = m + 1
            else:
                if m % 2:
                    l = m + 1
                else:
                    r = m - 1
            
        return nums[l] 