"""
1930. Unique Length-3 Palindromic Subsequences
Solved
Medium
Topics
Companies
Hint
Given a string s, return the number of unique palindromes of length three that are a subsequence of s.

Note that even if there are multiple ways to obtain the same subsequence, it is still only counted once.

A palindrome is a string that reads the same forwards and backwards.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
 

Example 1:

Input: s = "aabca"
Output: 3
Explanation: The 3 palindromic subsequences of length 3 are:
- "aba" (subsequence of "aabca")
- "aaa" (subsequence of "aabca")
- "aca" (subsequence of "aabca")
Example 2:

Input: s = "adc"
Output: 0
Explanation: There are no palindromic subsequences of length 3 in "adc".
Example 3:

Input: s = "bbcbaba"
Output: 4
Explanation: The 4 palindromic subsequences of length 3 are:
- "bbb" (subsequence of "bbcbaba")
- "bcb" (subsequence of "bbcbaba")
- "bab" (subsequence of "bbcbaba")
- "aba" (subsequence of "bbcbaba")
 

Constraints:

3 <= s.length <= 105
s consists of only lowercase English letters.

"""

class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        # time: O(n^3) | space: O(n)
        res = set()
        for i in range(len(s) - 2):
            for j in range(i + 1, len(s) - 1):
                for k in range(j + 1, len(s)):
                    if s[i] == s[k]:
                        res.add(s[i] + s[j] + s[k])
        
        return len(res)

        # time: O(26.n) | space: O(n)
        res = set()
        left = set()
        right = collections.Counter(s)

        for i in range(len(s)):

            right[s[i]] -= 1

            for j in range(26):
                c = chr(ord('a') + j)
                if c in left and (c in right and right[c] != 0):
                    res.add(c + s[i] + c)
            left.add(s[i])
        
        return len(res)

        # time: O(n) | space: O(n)
        res = 0
        count = {}

        for i in range(len(s)):
            if s[i] not in count:
                count[s[i]] = []
            count[s[i]].append(i)
        
        for k, v in count.items():
            if len(v) >= 2:
                res += len(set(s[v[0] + 1 : v[-1]]))
        
        return res

        