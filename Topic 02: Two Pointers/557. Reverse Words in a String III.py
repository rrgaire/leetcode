"""
557. Reverse Words in a String III
Solved
Easy
Topics
Companies
Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

 

Example 1:

Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Example 2:

Input: s = "Mr Ding"
Output: "rM gniD"
 

Constraints:

1 <= s.length <= 5 * 104
s contains printable ASCII characters.
s does not contain any leading or trailing spaces.
There is at least one word in s.
All the words in s are separated by a single space.

"""

class Solution:
    def reverseWords(self, s: str) -> str:

        l = 0
        k = 0
        slist = list(s)

        while k < len(s):
            while k < len(s) and s[k] != ' ':
                k += 1
            r = k - 1
            while l <= r:
                slist[l], slist[r] = slist[r], slist[l]
                l += 1
                r -= 1
            k += 1
            l = k

        return ''.join(slist)  