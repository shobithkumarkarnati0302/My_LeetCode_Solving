# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedListToBST(self, head):
        if not head:
            return None

        if not head.next:
            return TreeNode(head.val)

        prev = None
        slow = fast = head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        if prev:
            prev.next = None
        
        root = TreeNode(slow.val)
        root.left = self.sortedListToBST(head) 
        root.right = self.sortedListToBST(slow.next) 

        return root

        
        