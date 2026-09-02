class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack=[]
        for i in ops:
            if i =="C":
                toremove=stack.pop()
            elif i =="D":
                stack.append(int(stack[-1])*2)
            elif i =="+":
                val1=int(stack[-1] if stack else None)
                val2=int(stack[-2] if len(stack)>=2 else None)
                summed=val1+val2
                stack.append(summed)
            else:
                stack.append(int(i))
        return(sum(stack))