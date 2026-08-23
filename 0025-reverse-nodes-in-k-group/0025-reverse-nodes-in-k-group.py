class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr=head
        length=0
        while curr:
            length+=1
            curr=curr.next
        groups=length//k
        dummy=ListNode(0,head)
        curr=head
        prev=dummy
        for i in range(groups):
            for _ in range(k-1):
                tmp=curr.next
                curr.next=tmp.next
                tmp.next=prev.next
                prev.next=tmp
            prev=curr
            curr=curr.next
        return dummy.next