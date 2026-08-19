class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        prev=dummy
        curr=head

        while curr is not None and curr.next is not None:
            if curr.val == curr.next.val:
                while curr.next is not None and curr.val == curr.next.val:
                    curr=curr.next
                prev.next=curr.next
            else:
                prev=prev.next
            curr=curr.next
        return dummy.next