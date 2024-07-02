"""
131. Palindrome Partitioning
Solved
Medium
Topics
Companies
Given a string s, partition s such that every 
substring
 of the partition is a 
palindrome
. Return all possible palindrome partitioning of s.

 

Example 1:

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
Example 2:

Input: s = "a"
Output: [["a"]]
 

Constraints:

1 <= s.length <= 16
s contains only lowercase English letters.

"""

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        res = []
        part = []

        def ispalindrome(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        def backtrack(i):

            if i == len(s):
                res.append(part[:])
                return

            for j in range(i, len(s)):
                if ispalindrome(i, j):
                    part.append(s[i:j+1])
                    backtrack(j+1)
                    part.pop()
            
        backtrack(0)
        return res
        