"""

84. Largest Rectangle in Histogram
Hard

Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

 

Example 1:


Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.
Example 2:


Input: heights = [2,4]
Output: 4
 

Constraints:

1 <= heights.length <= 105
0 <= heights[i] <= 104

"""


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        # time: O(n) | space: O(n)
        maxarea = 0
        stack = []

        for i, ht in enumerate(heights):
            start = i
            while stack and ht < stack[-1][1]:
                index, height = stack.pop()
                area = (i-index) * height
                maxarea = max(maxarea, area)
                start = index
            stack.append((start, ht))

        for i, ht in stack:
            area = (len(heights) - i) * ht
            maxarea = max(maxarea, area)
        
        return maxarea