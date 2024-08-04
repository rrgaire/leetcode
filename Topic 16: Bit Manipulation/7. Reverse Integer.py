"""
7. Reverse Integer
Solved
Medium
Topics
Companies
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
 

Constraints:

-231 <= x <= 231 - 1

"""

class Solution:
    def reverse(self, x: int) -> int:

        # time : O(log(x)) | space: O(log(x))
        s = str(x)
        neg = False
        res = ''

        if s[0] == '-':
            neg = True
            s = s[1:]
        
        for c in s:
            res = c + res

        res = int(res)

        if res >= (2 ** 31 - 1):
            return 0

        return -res if neg else res

        # time : O(log(x)) | space: O(log(x))
        
        neg = False
        if x < 0:
            neg = True
            x = abs(x)
        res = 0
        while x:
            dig = x % 10
            res = res * 10 + dig
            if res > 2 ** 31 - 1:
                return 0

            x = x // 10
        
        return -res if neg else res
        
