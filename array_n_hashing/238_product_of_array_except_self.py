"""
238. Product of Array Except Self

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

"""



class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """


        # soln = []

        # for i in range(len(nums)):
        #     prod = 1
        #     for j in range(len(nums)):
        #         if i != j:
        #             prod *= nums[j]
        #     soln.append(prod)
        
        # return soln

        # soln = []
        # pre_prod = 1

        # for i in range(len(nums)):
        #     pre_prod *= nums[i]
        #     soln.append(pre_prod)
        # post_prod = nums[len(nums) - 1]

        # soln[len(nums) - 1] = soln[len(nums) - 2]
        
        # for i in range(len(nums) - 2, 0, -1):            
        #     soln[i] = soln[i-1] * post_prod
        #     post_prod *= nums[i]
        # soln[0] = post_prod
        
        # return soln


        soln = [1] * len(nums)

        prefix = 1

        for i in range(len(nums)):
            soln[i] = prefix
            prefix *= nums[i]

        postfix = 1

        print(soln)

        for i in range(len(nums)-1, -1, -1):
            soln[i] *= postfix
            postfix *= nums[i]

        return soln 

        
        