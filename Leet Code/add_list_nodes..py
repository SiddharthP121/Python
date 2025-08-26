# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        def to_number(node):
            place = 1
            num = 0
            while node:
                num += node.val * place
                place *= 10
                node = node.next
            return num

        def to_listnode(num):
            dummy = ListNode()
            current = dummy
            if num == 0:
                return ListNode(0)
            while num:
                current.next = ListNode(num % 10)
                num //= 10
                current = current.next
            return dummy.next


        num1 = to_number(l1)
        num2 = to_number(l2)
        total = num1 + num2
        return to_listnode(total)
