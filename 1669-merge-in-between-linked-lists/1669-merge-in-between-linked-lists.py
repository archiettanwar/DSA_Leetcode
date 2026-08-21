class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        slow=list1
        fast=list1
        for _ in range(a-1):
            slow=slow.next
        fast=slow
        for _ in range(b-a+1):
            fast=fast.next

        slow.next=list2

        tail2=list2
        while tail2.next:
            tail2=tail2.next
        tail2.next=fast.next
        return list1