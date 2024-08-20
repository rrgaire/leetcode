"""
1662. Check If Two String Arrays are Equivalent
Solved
Easy
Topics
Companies
Hint
Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false otherwise.

A string is represented by an array if the array elements concatenated in order forms the string.

 

Example 1:

Input: word1 = ["ab", "c"], word2 = ["a", "bc"]
Output: true
Explanation:
word1 represents string "ab" + "c" -> "abc"
word2 represents string "a" + "bc" -> "abc"
The strings are the same, so return true.
Example 2:

Input: word1 = ["a", "cb"], word2 = ["ab", "c"]
Output: false
Example 3:

Input: word1  = ["abc", "d", "defg"], word2 = ["abcddefg"]
Output: true
 

Constraints:

1 <= word1.length, word2.length <= 103
1 <= word1[i].length, word2[i].length <= 103
1 <= sum(word1[i].length), sum(word2[i].length) <= 103
word1[i] and word2[i] consist of lowercase letters.

"""

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:

        return ''.join(word1) == ''.join(word2)

        w1 = ''
        w2 = ''

        for w in word1:
            w1 += w
        
        for w in word2:
            w2 += w
        
        return w1 == w2

        w1 = w2 = 0
        i = j = 0

        while w1 < len(word1) and w2 < len(word2):
            if word1[w1][i] != word2[w2][j]:
                return False
            
            i += 1
            j += 1

            if i == len(word1[w1]):
                w1 += 1
                i = 0
            
            if j == len(word2[w2]):
                w2 += 1
                j = 0
        
        if w1 != len(word1) or w2 != len(word2):
            return False
        return True

        