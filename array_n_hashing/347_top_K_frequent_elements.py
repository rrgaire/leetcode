"""
347. Top K Frequent Elements
Medium

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.


"""

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        # hashmap = {}

        # for num in nums:
        #     if num in hashmap:
        #         hashmap[num] += 1
        #     else:
        #         hashmap[num] = 1

        # sorted_array = sorted(hashmap.items(), key=lambda kv: (kv[1], kv[0]), reverse=True)

        # return [x[0] for x in sorted_array[:k]]


        count = {}
        freq = [[] for _ in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)

        for n, c in count.items():
            freq[c].append(n)
        
        soln = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                soln.append(n)
                if len(soln) == k:
                    return soln