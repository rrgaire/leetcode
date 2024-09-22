"""
234. Palindrome Linked List
Solved
Easy
Topics
Companies
Given the head of a singly linked list, return true if it is a 
palindrome
 or false otherwise.

 

Example 1:


Input: head = [1,2,2,1]
Output: true
Example 2:


Input: head = [1,2]
Output: false
 

Constraints:

The number of nodes in the list is in the range [1, 105].
0 <= Node.val <= 9
 

Follow up: Could you do it in O(n) time and O(1) space?

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # time: O(n) | space: O(n)
        stack = []

        cur = head
        while cur:
            stack.append(cur.val)
            cur = cur.next
        
        cur = head

        while stack and cur:
            if stack.pop() != cur.val:
                return False
            cur = cur.next
        
        return True
        
        # time: O(n) | space: O(n)
        arr = []
        cur = head
        while cur:
            arr.append(cur.val)
            cur = cur.next
        
        l = 0
        r = len(arr) - 1

        while l <= r:
            if arr[l] != arr[r]:
                return False
            l += 1
            r -= 1
        return True

        # time: O(n) | space: O(1)

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        cur = slow
        prev = None

        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        
        left = head
        right = prev

        while left and right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True
