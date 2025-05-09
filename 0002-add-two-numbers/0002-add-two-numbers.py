class Solution(object):
    def addTwoNumbers(self, l1, l2):
        # Convert linked list l1 to an integer
        num1, num2 = 0, 0
        multiplier = 1
        while l1:
            num1 += l1.val * multiplier
            multiplier *= 10
            l1 = l1.next
        
        # Convert linked list l2 to an integer
        multiplier = 1
        while l2:
            num2 += l2.val * multiplier
            multiplier *= 10
            l2 = l2.next
        
        # Add the two numbers
        total = num1 + num2
        
        # Convert the result to a linked list in reverse order
        dummy = ListNode()
        current = dummy
        for digit in str(total)[::-1]:
            current.next = ListNode(int(digit))
            current = current.next

        return dummy.next
