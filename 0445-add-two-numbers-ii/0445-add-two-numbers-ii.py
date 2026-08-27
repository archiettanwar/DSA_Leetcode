class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = l1
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        reversed_l1 = prev

        prev = None
        curr = l2
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
            
        reversed_l2 = prev

        carry=0
        head=None
        while reversed_l1 or reversed_l2 or carry:
            val1=reversed_l1.val if reversed_l1 else 0
            val2=reversed_l2.val if reversed_l2 else 0

            total=val1+val2+carry
            carry=total//10

            new_node=ListNode(total%10)
            new_node.next=head
            head=new_node


            if reversed_l1:
                reversed_l1=reversed_l1.next
            if reversed_l2:
                reversed_l2=reversed_l2.next
        
        return head