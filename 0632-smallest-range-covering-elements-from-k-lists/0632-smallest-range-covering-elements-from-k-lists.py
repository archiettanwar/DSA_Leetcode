import heapq
from typing import List
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        minheap=[]
        left=right=nums[0][0]
        k=len(nums)
        for i in range(k):
            l=nums[i]
            left=min(left,l[0])
            right=max(right,l[0])
            heapq.heappush(minheap,(l[0],i,0))
        res=[left,right]

        while True:
            n,i,idx=heapq.heappop(minheap)
            idx+=1
            if idx == len(nums[i]):
                break
            nextval=nums[i][idx]
            heapq.heappush(minheap,(nextval,i,idx))
            right=max(right,nextval)
            left=minheap[0][0]

            if right-left<res[1]-res[0]:
                res=[left,right]
        return res
