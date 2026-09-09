class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        def get_size(node):
            size=0
            while node:
                size+=1
                node=node.next
            return size
        
        size = get_size(head)
        self.curr=head

        def build_tree(left,right):
            if left > right:
                return None
            mid = (left+right)//2
            leftchild=build_tree(left,mid-1)
            root=TreeNode(self.curr.val)
            root.left=leftchild

            self.curr=self.curr.next
            root.right=build_tree(mid+1,right)
            return root
        return build_tree(0,size-1)