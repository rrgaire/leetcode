"""
86. Partition List
Solved
Medium
Topics
Companies
Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

 

Example 1:


Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]
Example 2:

Input: head = [2,1], x = 2
Output: [1,2]
 

Constraints:

The number of nodes in the list is in the range [0, 200].
-100 <= Node.val <= 100
-200 <= x <= 200

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:

        # time: O(n) | space: O(1)
        
        left = ListNode(next= head)

        prev = left
        cur = head
        last = head
        while last and last.next:
            last = last.next

        end = last

        while cur:
            tmp = cur.next
            if cur == last:
                break

            if cur.val >= x:
                last.next = cur
                last = last.next
                prev.next = tmp
                last.next = None
                
            else:
                prev = cur

            if cur == end:
                break

            cur = tmp

        return left.next
        
        left, right = ListNode(), ListNode()
        ltail, rtail = left, right

        while head:
            if head.val < x:
                ltail.next = head
                ltail = ltail.next
            else:
                rtail.next = head
                rtail = rtail.next
            head = head.next
        
        ltail.next = right.next
        rtail.next = None

        return left.next