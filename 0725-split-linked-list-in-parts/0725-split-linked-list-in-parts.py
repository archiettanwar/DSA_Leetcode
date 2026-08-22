class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        curr = head
        N = 0
        while curr:
            N += 1
            curr = curr.next
        base_size = N // k
        extra = N % k
        
        result = []
        curr = head
        
        for i in range(k):
            result.append(curr)
            
            part_size = base_size + (1 if extra > 0 else 0)
            extra -= 1
            
            for _ in range(part_size - 1):
                if curr:
                    curr = curr.next
            if curr:
                next_node = curr.next
                curr.next = None
                curr = next_node
                
        return result