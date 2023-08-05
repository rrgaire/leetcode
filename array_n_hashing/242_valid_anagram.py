"""
242. Valid Anagram
Easy

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.

"""
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        anagram = False
        dict_t = dict()

        for b in t:
            if b in dict_t:
                dict_t[b] += 1
            else:
                dict_t[b] = 1

        for a in s:
            if a in dict_t:
                dict_t[a] -= 1
            else:
                return False


        for key in dict_t:
            if dict_t[key] != 0:
                return False
        
        return True
