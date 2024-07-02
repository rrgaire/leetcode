"""
295. Find Median from Data Stream
Solved
Hard
Topics
Companies
The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.

For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
Implement the MedianFinder class:

MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data structure.
double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.
 

Example 1:

Input
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
Output
[null, null, null, 1.5, null, 2.0]

Explanation
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3);    // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0
 

Constraints:

-105 <= num <= 105
There will be at least one element in the data structure before calling findMedian.
At most 5 * 104 calls will be made to addNum and findMedian.
 

Follow up:

If all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
If 99% of all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?

"""

# class MedianFinder:

#     def __init__(self):
#         self.array = []
        

#     def addNum(self, num: int) -> None:

#         # time: O(1) | sppace: O(n)
#         self.array.append(num)
        

#     def findMedian(self) -> float:

#         # time: O(nlogn) | sppace: O(1)
#         self.array = sorted(self.array)
#         mid = (len(self.array)-1) // 2
#         if len(self.array) % 2 == 1:
#             return self.array[mid]
#         else:
#             return (self.array[mid] + self.array[mid+1]) / 2


class MedianFinder:

    def __init__(self):
        self.minheap = []
        self.maxheap = []
        heapq.heapify(self.minheap)
        heapq.heapify(self.maxheap)

    def addNum(self, num: int) -> None:
        
        # time: O(logn) | sppace: O(n)
        if self.minheap and num <= self.minheap[0]:
            heapq.heappush(self.maxheap, -num)
        else:
            heapq.heappush(self.minheap, num)

        if len(self.maxheap) - len(self.minheap) > 1:
            heapq.heappush(self.minheap, -heapq.heappop(self.maxheap))
        elif len(self.minheap) - len(self.maxheap) > 1:
            heapq.heappush(self.maxheap, -heapq.heappop(self.minheap))

        

    def findMedian(self) -> float:
        
        # time: O(1) | sppace: O(1)
        if len(self.minheap) == len(self.maxheap):
            return (self.minheap[0] - self.maxheap[0]) / 2
        elif len(self.minheap) > len(self.maxheap):
            return self.minheap[0]
        else:
            return -self.maxheap[0]
 


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()