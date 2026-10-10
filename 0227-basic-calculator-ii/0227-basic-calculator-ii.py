class Solution:
    def calculate(self, s: str) -> int:
        if not s :
            return 0
            
        current_num = 0
        last_num = 0
        result = 0
        sign = '+'
        
        for i, char in enumerate(s):
            if char.isdigit():
                current_num = current_num * 10 + int(char)
                
            if char in "+-*/" or i == len(s) - 1:
                if sign == '+':
                    result += last_num
                    last_num = current_num
                elif sign == '-':
                    result += last_num
                    last_num = -current_num
                elif sign == '*':
                    last_num = last_num * current_num
                elif sign == '/':
                    last_num = int(last_num / current_num)
                
                sign = char
                current_num = 0
        result += last_num
        return result