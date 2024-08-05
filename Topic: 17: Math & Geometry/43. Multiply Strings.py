"""
43. Multiply Strings
Solved
Medium
Topics
Companies
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

 

Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"
 

Constraints:

1 <= num1.length, num2.length <= 200
num1 and num2 consist of digits only.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.

"""

class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        if '0' in [num1, num2]:
            return '0'

        n1 = len(num1)
        n2 = len(num2)

        res = [0] * (n1 + n2)
        
        for i in range(n2 - 1, -1, -1):
            for j in range(n1 - 1, -1, -1):
                prod = (int(num2[i]) * int(num1[j]))
                res[i+j+1] += prod
                res[i+j] += res[i+j+1] // 10
                res[i+j+1] = res[i+j+1] % 10

        i = 0
        while res[i] == 0:
            i += 1
        res = map(str, res[i:])
        return ''.join(res)



        # Alternative

    def multiply(self, num1: str, num2: str) -> str:

        if '0' in [num1, num2]:
            return '0'

        n1 = len(num1)
        n2 = len(num2)

        res = [0] * (n1 + n2)
        
        for i in range(n2 - 1, -1, -1):
            c1 = 0
            c2 = 0
            for j in range(n1 - 1, -1, -1):
                prod = (int(num2[i]) * int(num1[j])) + c1 + c2
                u1 = prod % 10
                c1 = prod // 10

                sum = res[i + j + 1] + u1
                u2 =  sum % 10
                c2 = sum // 10
                res[i + j + 1] = u2
            
            if c1:
                res[i + j] += c1
            if c2:
                res[i + j] += c2
                c2 = 0

        if c2:
            res[0] += c2

        i = 0
        while res[i] == 0:
            i += 1
        res = map(str, res[i:])
        return ''.join(res)