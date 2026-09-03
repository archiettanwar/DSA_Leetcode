class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        hmap={}
        stack=[]
        res=[]
        for i in nums2:
            while stack and i > stack[-1]:
                popped = stack.pop()
                hmap[popped] = i
            stack.append(i)
        for i in nums1:
            res.append(hmap.get(i,-1))
        return res