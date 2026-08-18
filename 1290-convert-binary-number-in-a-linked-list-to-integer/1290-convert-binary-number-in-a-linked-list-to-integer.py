class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        current=head
        count=(-1)
        while current:
            count+=1
            current=current.next
        current=head
        res=0
        while current:
            twoval=int(math.pow(2,count))
            res+=(twoval*(current.val))
            current=current.next
            count-=1
        return res