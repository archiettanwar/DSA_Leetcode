class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow,fast=head,head.next
        while fast is not None and fast.next is not None:
            slow=slow.next
            fast=fast.next.next
        second=slow.next
        prev=slow.next=None
        while second:
            tmp=second.next
            second.next=prev
            prev=second
            second=tmp
        first,second=head,prev
        while second is not None and first is not None:
            if first.val!=second.val:
                return False
            else:
                first=first.next
                second=second.next
        return True   