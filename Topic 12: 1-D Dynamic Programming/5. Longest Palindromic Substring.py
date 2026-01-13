"""
5. Longest Palindromic Substring
Solved
Medium
Topics
Companies
Hint
Given a string s, return the longest 
palindromic
 
substring
 in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.

"""

class Solution:

    def longestPalindrome(self, s: str) -> str:
        # Dynamic Programming: O(n^2) | O(n^2)
        res = 0
        l = 0
        r = 0

        dp = [[False] * len(s) for _ in range(len(s))]

        for i in range(len(s) - 1, -1, -1):
            for j in range(i, len(s)):
                if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1]):
                    if j - i + 1 >= res:
                        l = i
                        r = j
                    res = max(res, j - i + 1)
                    dp[i][j] = True
        
        return s[l:r + 1]

        # Two Pointer: O(n^2) | O(1)
        res = ''
        reslen = 0

        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r-l+1) > reslen:
                    res = s[l:r+1]
                    reslen = r - l + 1
                
                l -= 1
                r += 1
            
            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > reslen:
                    res = s[l:r+1]
                    reslen = r - l + 1
                
                l -= 1
                r += 1
            
        return res




        