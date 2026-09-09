class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        numset=set(nums)
        count=0
        curr=head

        while curr:
            if curr.val in numset and (not curr.next or curr.next.val not in numset):
                count+=1
            curr=curr.next
        
        return count