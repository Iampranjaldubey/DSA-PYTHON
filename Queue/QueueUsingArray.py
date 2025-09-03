
class Queue:

    def __init__(self,cap):
        self.queue = [None]*cap
        self.capacity = cap
        self.size = 0
        self.front = -1
        self.rear = -1

    def display(self):
        print("Queue is: ",end="")
        for i in range(self.front,self.size):
            print(self.queue[i],end=" ")
        print()

    def enqueue(self,item):
        print("Inserting element...",item)
        if(self.size==0):
            self.rear += 1 #rear = 0
            self.front = 0 #front = 0 
            self.queue[self.rear] = item
            self.size += 1 #1

        elif(self.size==self.capacity):
            print("cannot insert element, queue is full")
        else:
            self.rear += 1
            self.queue[self.rear] = item
            self.size +=1

        print(f"front={self.front}, rear={self.rear}")
    '''
    def dequeue(self):
        if(self.size==0):
            print("Queue empty, cannot delete")
        else:
            print("Deleting element: ",self.queue[self.front])
            self.size -= 1
            self.rear -= 1
            self.queue[]
    '''

q = Queue(5)

q.display()

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.display()

q.enqueue(4)
q.enqueue(5)
q.display()

q.enqueue(6)


