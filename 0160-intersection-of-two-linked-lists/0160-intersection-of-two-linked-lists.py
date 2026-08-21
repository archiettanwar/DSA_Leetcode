# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        myset=set()
        la=headA
        while la:
            myset.add(la)
            la=la.next
        lb=headB
        while lb:
            if lb not in myset:
                myset.add(lb)
            else:
                return lb
            lb=lb.next
        return 