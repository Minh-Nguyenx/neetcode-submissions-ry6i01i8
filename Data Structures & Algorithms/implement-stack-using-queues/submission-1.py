class MyStack:

    def __init__(self):
        # Khoi tao hang doi rong
        self.q = deque()

    def push(self, x: int) -> None:
        # Them phan tu vao cuoi 
        self.q.append(x)

    def pop(self) -> int:
        # Lap qua n - 1 phan tu
        for _ in range(len(self.q) - 1):
            # Xoay vong cac phan tu de dua phan tu cuoi len dau
            self.push(self.q.popleft())
        # Pop phan tu tren cung nhung vao cuoi cung
        return self.q.popleft()

    def top(self) -> int:
        # Tra ve phan tu cuoi hang
        return self.q[-1]

    def empty(self) -> bool:
        return len(self.q) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()