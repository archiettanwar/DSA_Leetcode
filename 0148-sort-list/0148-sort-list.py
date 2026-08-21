class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        def get_mid(head):
            slow,fast=head,head.next
            while fast is not None and fast.next is not None:
                slow=slow.next
                fast=fast.next.next
            return slow
        
        def merge(left,right):
            dummy=ListNode(0)
            tail=dummy
            while left is not None and right is not None:
                if left.val<=right.val:
                    tail.next=left 
                    left=left.next
                else:
                    tail.next=right
                    right=right.next
                tail=tail.next
            if left:
                tail.next=left
            if right:
                tail.next=right
            return dummy.next
        
        left=head
        right=get_mid(head)
        tmp=right.next
        right.next=None
        right=tmp

        left=self.sortList(left)
        right=self.sortList(right)

        return merge(left,right)