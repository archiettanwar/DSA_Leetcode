class CustomStack:
    def __init__(self, maxSize: int):
        self.stack = []
        self.inc_array = []
        self.maxSize = maxSize

    def push(self, x: int) -> None:
        if len(self.stack) < self.maxSize:
            self.stack.append(x)
            self.inc_array.append(0)

    def pop(self) -> int:
        if not self.stack:
            return -1
        
        # Get the pending increment for the top element
        inc_val = self.inc_array.pop()
        
        # If there are still elements left, pass the increment down to the next top element
        if self.inc_array:
            self.inc_array[-1] += inc_val
            
        # Return the actual value + its increment
        return self.stack.pop() + inc_val

    def increment(self, k: int, val: int) -> None:
        if self.stack:
            # Find the index of the top-most element that should receive the increment
            idx = min(k - 1, len(self.stack) - 1)
            self.inc_array[idx] += val
