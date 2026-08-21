class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        def get_mid(node):
            slow = node
            fast = node.next
            while fast is not None and fast.next is not None:
                slow = slow.next
                fast = fast.next.next
            return slow
        
        def mergeList(left_node, right_node):
            dummy = ListNode(0)
            tail = dummy
            while left_node is not None and right_node is not None:
                if left_node.val <= right_node.val:
                    tail.next = left_node
                    left_node = left_node.next
                else:
                    tail.next = right_node
                    right_node = right_node.next
                tail = tail.next
            if left_node:
                tail.next = left_node 
            if right_node:
                tail.next = right_node
            return dummy.next
            
        left = head
        mid = get_mid(head)
        right = mid.next
        mid.next = None

        left = self.sortList(left)
        right = self.sortList(right)

        return mergeList(left, right)