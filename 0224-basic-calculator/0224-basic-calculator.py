
class Solution:
    def calculate(self, s: str) -> int:
        res = 0
        num = 0
        sign = 1
        stack = [sign]
        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c == '+':
                res += sign * num
                sign = stack[-1]
                num = 0
            elif c == '-':
                res += sign * num
                sign = -stack[-1]
                num = 0
            elif c == '(':
                stack.append(sign)
            elif c == ')':
                stack.pop()
                
        return res + sign * num