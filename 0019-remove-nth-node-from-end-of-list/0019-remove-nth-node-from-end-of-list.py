# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, k):
        temp = head
        count = 0
        while temp:
            temp = temp.next
            count += 1
        
        pos = count - k
        if pos == 0:
            return head.next
            
        temp1 = head
        for i in range(pos-1):
            temp1 = temp1.next
    
        temp1.next = temp1.next.next

        return head
        

        