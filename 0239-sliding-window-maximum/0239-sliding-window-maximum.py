from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        q= deque()
        res=[]

        for i,num in enumerate(nums):
            while q and nums[q[-1]]<num:
                q.pop()
            if q and q[0]<=i-k:
                q.popleft()
            q.append(i)
            if i>=k-1:
                res.append(nums[q[0]])
        return res