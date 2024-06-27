"""
215. Kth Largest Element in an Array
Solved
Medium
Topics
Companies
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?

 

Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
 

Constraints:

1 <= k <= nums.length <= 105
-104 <= nums[i] <= 104

"""

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # # time: O(nlogn) | space: O(1)
        # nums = sorted(nums)
        # return nums[-k]
        
        # # time: O(n + klogn) | space: O(1)
        # nums = [-x for x in nums]
        # heapq.heapify(nums)
        # while k > 1:
        #     heapq.heappop(nums)
        #     k -= 1
        
        # return -nums[0]

        # time: O(n2), Q(n) | space: O(1)

        k = len(nums) - k
        l = 0
        r = len(nums) - 1

        def partition(l, r):
            pivot = nums[r]
            fill = l

            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[i], nums[fill] = nums[fill], nums[i]
                    fill += 1
            
            nums[fill], nums[r] = nums[r], nums[fill]
            return fill
    
        while l < r:
            pivot = partition(l, r)
            if pivot < k:
                l = pivot + 1
            elif pivot > k:
                r = pivot - 1
            else:
                break
        return nums[k]
            
   