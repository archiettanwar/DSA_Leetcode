class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        curr=head
        while curr:
            if curr.child:
                tail=curr.child
                while tail.next:
                    tail=tail.next
                if curr.next:
                    curr.next.prev=tail
                    tail.next=curr.next
                curr.next=curr.child
                curr.child.prev=curr
                curr.child=None
            curr=curr.next
        return head