"""

128. Longest Consecutive Sequence

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
 

"""

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # hash_nums = dict()

        # for num in nums:
        #     if num not in hash_nums:
        #         hash_nums[num] = 0
        # max = 0
        # for key in hash_nums:
        #     if key-1 not in hash_nums:
        #         count = 1
        #         while (key+1) in hash_nums:
        #             count += 1
        #             key += 1
        #         if count > max:
        #             max = count
        # return max

        hash_nums = set(nums)
        longest = 0
        for num in hash_nums:
            if num-1 not in hash_nums:
                count = 1
                while (num+count) in hash_nums:
                    count += 1
                longest = max(count, longest)

        return longest
