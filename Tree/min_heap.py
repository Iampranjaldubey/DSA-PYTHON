class MinHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2
    
    def left(self, i):
        return 2 * i + 1
    
    def right(self, i):
        return 2 * i + 2

    def insert(self, key):
        """Insert a new key into the heap"""
        self.heap.append(key)
        i = len(self.heap) - 1
        # Fix the min heap property if it's violated
        while i != 0 and self.heap[self.parent(i)] > self.heap[i]:
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)

    def heapify(self, i):
        """Corrects the heap starting from index i"""
        l = self.left(i)
        r = self.right(i)
        smallest = i

        if l < len(self.heap) and self.heap[l] < self.heap[smallest]:
            smallest = l
        if r < len(self.heap) and self.heap[r] < self.heap[smallest]:
            smallest = r

        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self.heapify(smallest)

    def extract_min(self):
        """Remove and return the minimum element (root)"""
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        
        root = self.heap[0]
        self.heap[0] = self.heap.pop()  # Move last to root and heapify
        self.heapify(0)
        return root

    def get_min(self):
        """Return the minimum element without removing it"""
        if self.heap:
            return self.heap[0]
        return None

    def __str__(self):
        return str(self.heap)

# Example usage
heap = MinHeap()
heap.insert(3)
heap.insert(1)
heap.insert(6)
heap.insert(5)
heap.insert(2)
heap.insert(4)

print("Heap:", heap)
print("Extracted min:", heap.extract_min())
print("Heap after extraction:", heap)
