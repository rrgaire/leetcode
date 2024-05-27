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
        # time: O(n) | space: O(n)
        maxlen = 0
        hashset = set(nums)

        for num in hashset:
            if num-1 not in hashset:
                count = 1
                while num+count in hashset:
                    count += 1
                if count > maxlen:
                    maxlen = count
        return maxlen
