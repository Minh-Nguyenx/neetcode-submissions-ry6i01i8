class MyHashSet:

    def __init__(self):
        self.size = 1000
        self.buckets = [None] * self.size
        self.count = 0

    def hash(self, key: int):
        # Bam so nguyen bat ky vao mang
        return key % self.size

    def rehash(self):
        old_buckets = self.buckets
        self.size *= 2
        self.buckets = [None] * self.size
        self.count = 0

        for i in range(len(old_buckets)):
            cur = old_buckets[i]
            while cur:
                self.add(cur.data)
                cur = cur.next

    def add(self, key: int) -> None:
        idx = self.hash(key)      
        # 1. Trường hợp ngăn rỗng
        if self.buckets[idx] is None:
            self.buckets[idx] = Node(key)
            self.count += 1
            if self.count / self.size > 0.75: # Neu load factor > 75% thi mo rong nha
                self.rehash()
            return
        
        # 2. Trường hợp có va chạm (duyệt danh sách)
        cur = self.buckets[idx]
        while cur:
            if cur.data == key:     # Đã tồn tại -> Dừng
                return
            elif cur.next is None:  # Đến cuối -> Thêm mới
                cur.next = Node(key)
                self.count += 1
                if self.count / self.size > 0.75:
                    self.rehash()
                return
            cur = cur.next          # Đi tiếp

    def remove(self, key: int) -> None:
        idx = self.hash(key)
        if self.buckets[idx] is None:
            return        
        elif self.buckets[idx].data == key:
            self.buckets[idx] = self.buckets[idx].next
            self.count -= 1
            return
        cur = self.buckets[idx]    
        while cur.next:
            if cur.next.data == key:
                cur.next = cur.next.next
                self.count -= 1
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