class MinStack:

    def __init__(self):
        self.ms = []
        self.m = []
    def push(self, val: int) -> None:        
        if len(self.ms) == 0:
            self.m.append(val)
        elif self.m[-1] >= val:          
            self.m.append(val)
        self.ms.append(val)

    def pop(self) -> None:
        n = self.ms.pop()
        if self.m[-1] == n:
            self.m.pop()

    def top(self) -> int:
        return self.ms[-1]

    def getMin(self) -> int:
        return self.m[-1]
