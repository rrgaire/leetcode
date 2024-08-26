"""
42. Trapping Rain Water
Hard
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Example 1:


Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9
 

Constraints:

n == height.length
1 <= n <= 2 * 104
0 <= height[i] <= 105

"""


class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        # time: O(n) | space: O(1)
        res = 0
        l = 0
        r = len(height) - 1
        max_L = height[l]
        max_R = height[r]

        while l < r:
            if max_L < max_R:
                l += 1
                max_L = max(max_L, height[l])
                res += max_L - height[l]
            else:
                r -= 1
                max_R = max(max_R, height[r])
                res += max_R - height[r]
        return res
    

class Solution:
    def trap(self, height: List[int]) -> int:
        maxr = [0] * len(height)

        for i in range(len(height) - 1, 0, -1):
            if height[i] > maxr[i]:
                maxr[i - 1] = height[i]
            else:
                maxr[i - 1] = maxr[i]

        res = 0
        maxl = height[0]

        for i in range(1, len(height)):
            amt = (min(maxl, maxr[i]) - height[i])
            res += amt if amt > 0 else 0
            maxl = max(maxl, height[i])
            
        return res

        