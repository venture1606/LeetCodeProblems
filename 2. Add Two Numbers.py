# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def coverting_number(node):
            number = ''
            current = node
            while current is not None:
                number += str(current.val)
                current = current.next
            return int(number[::-1])

        def making_listNode(answer):
            dummy_head = ListNode()
            current = dummy_head

            for x in answer:
                current.next = ListNode(int(x))
                current = current.next

            return dummy_head.next

        l1 = coverting_number(l1)
        l2 = coverting_number(l2)

        total = l1 + l2
        answer = str(total)[::-1]
        answer = making_listNode(answer)
        return answer
        
