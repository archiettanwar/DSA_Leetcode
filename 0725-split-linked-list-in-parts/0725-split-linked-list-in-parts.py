class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        curr=head
        length=0
        while curr :
            length+=1
            curr = curr.next
        base_size = length // k
        extra_size = length % k
        res = []
        curr = head
        for i in range(k):
            res.append(curr)
            part_size = base_size + (1 if extra_size>0  else 0)
            extra_size-=1
            for _ in range(part_size - 1):
                if curr:
                    curr = curr.next
            if curr:
                next_node = curr.next
                curr.next = None
                curr = next_node
        return res