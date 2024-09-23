"""
2487. Remove Nodes From Linked List
Solved
Medium
Topics
Companies
Hint
You are given the head of a linked list.

Remove every node which has a node with a greater value anywhere to the right side of it.

Return the head of the modified linked list.

 

Example 1:


Input: head = [5,2,13,3,8]
Output: [13,8]
Explanation: The nodes that should be removed are 5, 2 and 3.
- Node 13 is to the right of node 5.
- Node 13 is to the right of node 2.
- Node 8 is to the right of node 3.
Example 2:

Input: head = [1,1,1,1]
Output: [1,1,1,1]
Explanation: Every node has value 1, so no nodes are removed.
 

Constraints:

The number of the nodes in the given list is in the range [1, 105].
1 <= Node.val <= 105

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # time: O(n) | space: O(n)
        stack = []

        curr = head

        while curr:

            while stack and stack[-1] < curr.val:
                stack.pop()
            stack.append(curr.val)
            curr = curr.next
        dummy = ListNode()
        curr = dummy
        for v in stack:
            curr.next = ListNode(val=v)
            curr = curr.next
        
        return dummy.next

        # time: O(n) | space: O(1)


        def reverse(head):
            prev = None
            curr = head

            while curr:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            
            return prev
        
        head = reverse(head)

        curr = head
        curmax = curr.val
        while curr.next:
            if curr.next.val < curmax:
                curr.next = curr.next.next
            else:
                curmax = curr.next.val
                curr = curr.next
        
        return reverse(head)
            
        
        