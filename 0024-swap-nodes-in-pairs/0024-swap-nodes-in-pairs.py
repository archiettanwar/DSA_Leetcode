class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        prev=dummy
        curr=head

        while curr and curr.next:
            nextpair=curr.next.next
            second=curr.next

            second.next=curr
            curr.next=nextpair
            prev.next=second

            prev=curr
            curr=nextpair
        
        return dummy.next