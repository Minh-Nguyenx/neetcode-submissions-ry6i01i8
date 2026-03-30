class MyHashSet:

    def __init__(self):
        self.size = 1000
        self.buckets = [None] * self.size

    def hash(self, key: int):
        # Bam so nguyen bat ky vao mang
        return key % self.size

    def add(self, key: int) -> None:
        idx = self.hash(key)
        # 1. Trường hợp ngăn rỗng
        if self.buckets[idx] is None:
            self.buckets[idx] = Node(key)
            return
        
        # 2. Trường hợp có va chạm (duyệt danh sách)
        cur = self.buckets[idx]
        while cur:
            if cur.data == key:     # Đã tồn tại -> Dừng
                return
            elif cur.next is None:  # Đến cuối -> Thêm mới
                cur.next = Node(key)
                return
            cur = cur.next          # Đi tiếp

    def remove(self, key: int) -> None:
        idx = self.hash(key)
        if self.buckets[idx] is None:
            return        
        elif self.buckets[idx].data == key:
            self.buckets[idx] = self.buckets[idx].next
            return
        cur = self.buckets[idx]    
        while cur.next:
            if cur.next.data == key:
                cur.next = cur.next.next
                return
            cur = cur.next             

    def contains(self, key: int) -> bool:
        idx = self.hash(key)
        cur = self.buckets[idx]
        while cur:
            if cur.data == key:
                return True
            cur = cur.next
        return False
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)