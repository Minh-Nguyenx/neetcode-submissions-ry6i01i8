class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class MyHashMap:

    def __init__(self):
        self.size = 1000
        self.buckets = [None] * self.size

    def hash(self, key):
        return key % self.size

    def put(self, key: int, value: int) -> None:
        idx = self.hash(key)
        if self.buckets[idx] is None:
            self.buckets[idx] = Node(key, value)
            return
        cur = self.buckets[idx]
        while cur:
            if cur.key == key:
                cur.value = value
                return
            if cur.next is None:
                cur.next = Node(key, value)
                return
            cur = cur.next

    def get(self, key: int) -> int:
        idx = self.hash(key)
        cur = self.buckets[idx]
        while cur:
            if cur.key == key:
                return cur.value
            cur = cur.next
        return -1
    def remove(self, key: int) -> None:
        idx = self.hash(key)
        if self.buckets[idx] is None:
            return
        if self.buckets[idx].key == key:
            self.buckets[idx] = self.buckets[idx].next
            return
        cur = self.buckets[idx]
        while cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return
            cur = cur.next
# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)