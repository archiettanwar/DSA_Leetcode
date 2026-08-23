class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        fast=head
        for _ in range(k-1):
            fast=fast.next
        firstnode=fast
        slow=head
        while fast.next:
            slow=slow.next
            fast=fast.next
        secondnode=slow

        firstnode.val,secondnode.val=secondnode.val,firstnode.val

        return head