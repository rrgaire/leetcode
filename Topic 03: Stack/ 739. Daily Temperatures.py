"""
739. Daily Temperatures
Medium
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

 

Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
Example 2:

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
Example 3:

Input: temperatures = [30,60,90]
Output: [1,1,0]
 

Constraints:

1 <= temperatures.length <= 105
30 <= temperatures[i] <= 100

"""

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        # # time: O(n^2) | space: O(n)
        # res = []

        # for i, t in enumerate(temperatures):
        #     count = 0
        #     for j in range(i, len(temperatures)):
        #         if temperatures[j] > temperatures[i]:
        #             count = j - i
        #             break
        #     res.append(count)
        # return res

        # time: O(n) | space: O(n)
        res = [0] * len(temperatures)
        stack = []
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                res[stack[-1][1]] = i - stack[-1][1]
                stack.pop()
            stack.append([t, i])
        return res

            
