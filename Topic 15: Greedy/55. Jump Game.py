"""
55. Jump Game
Solved
Medium
Topics
Companies
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

 

Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
 

Constraints:

1 <= nums.length <= 104
0 <= nums[i] <= 105

"""

class Solution:
    def canJump(self, nums: List[int]) -> bool:

        # Dynamic Programming: time: O(n^2) | space: O(n)
        dp = {}

        def backtrack(i):
            if i == len(nums) - 1:
                return True
            
            for j in range(1, nums[i] + 1):
                if backtrack(i+j):
                    dp[i] = True
                    return dp[i]
            
            dp[i] = False
            return dp[i]
        return backtrack(0)

        # Greedy: time: O(n) | space: O(1)

        a = 0
        flag = False
        for i in range(len(nums) - 2, -1, -1):
            if not flag and nums[i] == 0:
                a = 1
                flag = True
            elif nums[i] > a:
                flag = False
                a = 0
            else:
                a += 1
            print(nums[i], a, flag)
        return not flag
            
        # time: O(n) | space: O(1)
        goal = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        
        return not goal