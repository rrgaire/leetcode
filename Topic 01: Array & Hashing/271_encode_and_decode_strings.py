
"""
String Encode and Decode

Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

Please implement encode and decode

Example 1:

Input: ["neet","code","love","you"]

Output:["neet","code","love","you"]
Example 2:

Input: ["we","say",":","yes"]

Output: ["we","say",":","yes"]
Constraints:

0 <= strs.length < 100
0 <= strs[i].length < 200
strs[i] contains only UTF-8 characters.

"""

class Solution:

    # time: O(n): space: O(n)
    def encode(self, strs):

        encoded_str = ""
        for word in strs:
            encoded_str += (str(len(word)) + '#' + word)
        return encoded_str

    # time: O(n): space: O(n)
    def decode(self, s):
        
        strs = []
        i = 0
        while i < len(s):
            j = i
            while s[j+1] != '#':
                j += 1
            length = int(s[i:j+1])
            word = s[j+2:j+2+length]
            strs.append(word)
            i = j + 2 + length
        return strs