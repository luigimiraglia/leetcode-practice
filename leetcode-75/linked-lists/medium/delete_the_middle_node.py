# Problem: Delete the Middle Node of a Linked List
# Link: https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/
# Difficulty: Medium
# Approach: Slow and fast pointers to get the central node
# Remove the central node
# Handle edge cases
# Time complexity O(n), Space complexity O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return None

        slow, fast = head, head.next.next

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        slow.next = slow.next.next

        return head
