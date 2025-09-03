class Queue:

    def __init__(self,cap):
        self.queue = [None]*cap
        self.size = 0
        self.front = -1
        self.rear = -1
        self.capacity = cap

    def display(self):
        print("Queue: ",self.queue)

    def enqueue(self,item):
        if(self.size==self.capacity):
            print("Cannot not insert element, queue full")
        else:
            print("Insering item:",item)
            if(self.front==-1):
                self.front = 0
            self.rear += 1
            self.queue[self.rear]=item
            self.size += 1
                
            

q = Queue(5)
q.display()

q.enqueue(1)
q.enqueue(2)
q.display()

