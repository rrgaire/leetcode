"""49. Group Anagrams
Medium

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
 

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters."""


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        # hash_list = []
        # soln_list = []

        # for word in strs:
        #     w_hash = {}
        #     for letter in word:
        #         if letter in w_hash:
        #             w_hash[letter] += 1
        #         else:
        #             w_hash[letter] = 1
        #     if w_hash in hash_list:
        #         idx = hash_list.index(w_hash)
        #         soln_list[idx].append(word)
        #     else:
        #         hash_list.append(w_hash)
        #         soln_list.append([word])

        # return soln_list


        hashmap = {}
        for word in strs:
            l_count = [0] * 26
            for letter in word:
                l_count[ord(letter) - ord('a')] += 1
            l_count = tuple(l_count)
            if l_count in hashmap:
                hashmap[l_count].append(word)
            else:
                hashmap[l_count] = [word]

        return list(hashmap.values())

