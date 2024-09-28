"""
148. Sort List
Solved
Medium
Topics
Companies
Given the head of a linked list, return the list after sorting it in ascending order.

 

Example 1:


Input: head = [4,2,1,3]
Output: [1,2,3,4]
Example 2:


Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]
Example 3:

Input: head = []
Output: []
 

Constraints:

The number of nodes in the list is in the range [0, 5 * 104].
-105 <= Node.val <= 105
 

Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)?

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return head
        
        mid = self.findmid(head)
        tmp = mid.next
        mid.next = None
        lhead = head
        rhead = tmp
        
        left = self.sortList(lhead)
        right = self.sortList(rhead)

        return self.merge(left, right)

    def findmid(self, head):
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow
    
    def merge(self, left, right):

        dummy = ListNode()
        cur = dummy

        while left and right:
            if left.val <= right.val:
                cur.next = ListNode(val= left.val)
                left = left.next
            else:
                cur.next = ListNode(val= right.val)
                right = right.next
            cur = cur.next
        
        if left:
            cur.next = left
        if right:
            cur.next = right
            
        return dummy.next