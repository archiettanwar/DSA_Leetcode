class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        res=[0]*len(temperatures)
        for i,temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                popped = stack.pop()
                res[popped]=i-popped
            stack.append(i)
        return res
