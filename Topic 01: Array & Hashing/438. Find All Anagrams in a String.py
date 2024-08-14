"""
438. Find All Anagrams in a String
Solved
Medium
Topics
Companies
Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
 

Constraints:

1 <= s.length, p.length <= 3 * 104
s and p consist of lowercase English letters.

"""

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        res = []
        count_p = {}
        count_s = {}

        for c in p:
            count_p[c] = 1 + count_p.get(c, 0)
        
        for i in range(len(s)):
            count_s[s[i]] = 1 + count_s.get(s[i], 0)
            if count_s == count_p:
                res.append(i - len(p) + 1)
        
            if (i - len(p) + 1) >= 0:
                if count_s[s[i - len(p) + 1]] != 0:
                    count_s[s[i - len(p) + 1]] -= 1
                if count_s[s[i - len(p) + 1]] == 0:
                    count_s.pop(s[i - len(p) + 1])
        return res


        