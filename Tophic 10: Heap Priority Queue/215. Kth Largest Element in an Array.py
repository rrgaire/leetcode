class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # # time: O(nlogn) | space: O(1)
        # nums = sorted(nums)
        # return nums[-k]

        # time: O(n + klogn) | space: O(1)
        heapq.heapify(nums)
        while len(nums) > k:
            heapq.heappop(nums)
        return nums[0]


        # # time: O(n2), Q(n) | space: O(1)

        # k = len(nums) - k
        # l = 0
        # r = len(nums) - 1

        # def partition(l, r):
        #     pivot = nums[r]
        #     fill = l

        #     for i in range(l, r):
        #         if nums[i] <= pivot:
        #             nums[i], nums[fill] = nums[fill], nums[i]
        #             fill += 1
            
        #     nums[fill], nums[r] = nums[r], nums[fill]
        #     return fill
    
        # while l < r:
        #     pivot = partition(l, r)
        #     if pivot < k:
        #         l = pivot + 1
        #     elif pivot > k:
        #         r = pivot - 1
        #     else:
        #         break
        # return nums[k]
            
