# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteNode(self, node):
        temp1 = node
        temp2 = node.next
        
        temp1.val,temp2.val = temp2.val,temp1.val

        temp1.next = temp1.next.next
