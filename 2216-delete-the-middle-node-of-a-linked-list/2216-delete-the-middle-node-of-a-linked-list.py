# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        if head is None or head.next is None:
            return None
        count = 0
        temp = head
        while temp:
            temp = temp.next
            count += 1
        mid = count // 2

        temp = head
        for i in range(mid-1):
            temp = temp.next

        temp.next = temp.next.next
        return head