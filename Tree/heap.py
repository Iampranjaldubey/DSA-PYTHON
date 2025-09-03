class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, val):
        """Insert value into the heap and maintain max-heap property."""
        self.heap.append(val)
        self._heapify_up(len(self.heap) - 1)

    def delete(self):
        """Remove and return the maximum value (root) from the heap."""
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        
        root = self.heap[0]
        self.heap[0] = self.heap.pop()  # Move last to root
        self._heapify_down(0)
        return root

    def _heapify_up(self, index):
        """Ensure the max-heap property is maintained going up."""
        parent = (index - 1) // 2
        if index > 0 and self.heap[index] > self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self._heapify_up(parent)

    def _heapify_down(self, index):
        """Ensure the max-heap property is maintained going down."""
        largest = index
        left = 2 * index + 1
        right = 2 * index + 2
        size = len(self.heap)

        if left < size and self.heap[left] > self.heap[largest]:
            largest = left
        if right < size and self.heap[right] > self.heap[largest]:
            largest = right
        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self._heapify_down(largest)

    def get_max(self):
        """Return the maximum value (root) without removing it."""
        return self.heap[0] if self.heap else None

    def display(self):
        """Print the current state of the heap."""
        print("Heap:", self.heap)


# ✅ Example Usage:
if __name__ == "__main__":
    h = MaxHeap()
    h.insert(10)
    h.insert(20)
    h.insert(5)
    h.insert(30)
    h.insert(15)

    h.display()           # Heap: [30, 15, 5, 10, 20]
    print(h.get_max())    # 30
    print(h.delete())     # 30
    h.display()           # Heap after deletion
