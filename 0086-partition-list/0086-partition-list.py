class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        lesser_node=ListNode(0)
        greater_node=ListNode(0)

        less=lesser_node
        greater=greater_node

        curr=head
        while curr:
            if curr.val<x:
                less.next=curr
                less=less.next
            else:
                greater.next=curr
                greater=greater.next
            curr=curr.next
        greater.next=None
        less.next=greater_node.next
        return lesser_node.next