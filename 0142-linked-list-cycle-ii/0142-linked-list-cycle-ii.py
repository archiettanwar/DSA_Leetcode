
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        myset=set()
        curr=head
        while curr is not None:
            if curr in myset:
                return curr
            myset.add(curr)
            curr=curr.next
        return None      