class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack=[]

        for i in s:
            top=stack[-1] if stack else None
            if top!=i:
                stack.append(i)
            elif top==i:
                stack.pop()

        res="".join(stack)
        return (res)