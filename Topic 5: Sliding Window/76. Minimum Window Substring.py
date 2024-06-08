"""
76. Minimum Window Substring
Solved
Hard
Topics
Companies
Hint
Given two strings s and t of lengths m and n respectively, return the minimum window 
substring
 of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

 

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
 

Constraints:

m == s.length
n == t.length
1 <= m, n <= 105
s and t consist of uppercase and lowercase English letters.

"""

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # res = ''
        # minLen = float('infinity')
        # if len(s) < len(t):
        #     return res

        # count_t = {}

        # for i in range(len(t)):
        #     count_t[t[i]] = 1 + count_t.get(t[i], 0)
    
        # l = 0
        # while l < len(s):
        #     while l < len(s) and s[l] not in count_t:
        #         l += 1
        #     r = l
        #     condn = 0
        #     count_s = {}

        #     while r < len(s):
        #         if s[r] in count_t:
        #             count_s[s[r]] = 1 + count_s.get(s[r], 0)
        #             if count_s[s[r]] == count_t[s[r]]:
        #                 condn += 1

        #         curLen = r - l + 1
        #         if condn == len(count_t) and curLen < minLen:
        #             minLen = curLen
        #             res = s[l:r+1]
        #             break
                    
        #         r += 1
        #     l += 1
            
        res = ''
        minLen = float('infinity')
        if len(s) < len(t):
            return res

        count_t = {}
        count_s = {}

        for i in range(len(t)):
            count_t[t[i]] = 1 + count_t.get(t[i], 0)
    
        l = 0
        condn = 0
        for r in range(len(s)):
            if s[r] in count_t:
                count_s[s[r]] = 1 + count_s.get(s[r], 0)
                if count_s[s[r]] == count_t[s[r]]:
                    condn += 1            
            
            while condn == len(count_t):
                curLen = r - l
                if curLen < minLen:
                    minLen = curLen
                    res = s[l:r+1]

                if s[l] in count_s:
                    count_s[s[l]] -= 1
                    if count_s[s[l]] < count_t[s[l]]:
                        condn -= 1

                l += 1

        return res     
        