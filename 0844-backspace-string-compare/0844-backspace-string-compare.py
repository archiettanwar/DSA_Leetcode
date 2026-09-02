class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1=[]
        stack2=[]

        for i in range(len(s)):
            if s[i] == "#":
                stack1.pop() if stack1 else None
            else :
                stack1.append(s[i])
                
        for i in range(len(t)):
            if t[i] == "#":
                    stack2.pop() if stack2 else None
            else:
                stack2.append(t[i])

        return("".join(stack1)=="".join(stack2))