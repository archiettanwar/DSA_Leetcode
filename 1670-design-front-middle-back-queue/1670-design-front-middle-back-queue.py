class FrontMiddleBackQueue:
    def __init__(self):
        # main[-1] is the back of the queue, main[0] is the front
        self.main = []
        self.helper = []

    def pushFront(self, val: int) -> None:
        while self.main:
            self.helper.append(self.main.pop())
        self.main.append(val)
        while self.helper:
            self.main.append(self.helper.pop())

    def pushMiddle(self, val: int) -> None:
        target_idx = len(self.main) // 2
        while len(self.main) > target_idx:
            self.helper.append(self.main.pop())
        self.main.append(val)
        while self.helper:
            self.main.append(self.helper.pop())

    def pushBack(self, val: int) -> None:
        self.main.append(val)

    def popFront(self) -> int:
        if not self.main:
            return -1
        while len(self.main) > 1:
            self.helper.append(self.main.pop())
        val = self.main.pop()
        while self.helper:
            self.main.append(self.helper.pop())
        return val

    def popMiddle(self) -> int:
        if not self.main:
            return -1
        target_idx = (len(self.main) - 1) // 2
        while len(self.main) > target_idx + 1:
            self.helper.append(self.main.pop())
        val = self.main.pop()
        while self.helper:
            self.main.append(self.helper.pop())
        return val

    def popBack(self) -> int:
        if not self.main:
            return -1
        return self.main.pop()