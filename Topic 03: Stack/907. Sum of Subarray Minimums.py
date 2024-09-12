"""
907. Sum of Subarray Minimums
Solved
Medium
Topics
Companies
Given an array of integers arr, find the sum of min(b), where b ranges over every (contiguous) subarray of arr. Since the answer may be large, return the answer modulo 109 + 7.

 

Example 1:

Input: arr = [3,1,2,4]
Output: 17
Explanation: 
Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4]. 
Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.
Sum is 17.
Example 2:

Input: arr = [11,81,94,43,3]
Output: 444
 

Constraints:

1 <= arr.length <= 3 * 104
1 <= arr[i] <= 3 * 104

"""

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:

        stack = []
        res = 0

        MOD = 10 ** 9 + 7

        for i, n in enumerate(arr):
            while stack and n < arr[stack[-1]]:
                idx = stack.pop()
                res += (arr[idx] * (i - idx) * (idx - (stack[-1] if stack else -1)))
            stack.append(i)
        
        while stack:
            idx = stack.pop()
            res += (arr[idx] * (len(arr) - idx) * (idx - (stack[-1] if stack else -1)))
        
        return res % MOD