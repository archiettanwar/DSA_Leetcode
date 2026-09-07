class RecentCounter:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def ping(self, t: int) -> int:
        self.in_stack.append(t)
        while True:
            if self.out_stack:
                if self.out_stack[-1] < t - 3000:
                    self.out_stack.pop()
                else:
                    break 
            else:
                if not self.in_stack:
                    break
                while self.in_stack:
                    self.out_stack.append(self.in_stack.pop())
        return len(self.in_stack) + len(self.out_stack)