class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        length=0
        curr=head
        while curr is not None:
            length+=1
            curr=curr.next
        curr=head
        dummy=ListNode(0,head)
        prev=dummy
        groups=length//k
        for _ in range(groups):
            for _ in range(k-1):
                temp=curr.next
                curr.next=temp.next
                temp.next=prev.next
                prev.next=temp
            prev=curr
            curr=curr.next
        return dummy.next