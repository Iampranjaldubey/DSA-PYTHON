class Queue:
    def __init__(self):
        self.queue = []

    def display(self):
        if(len(self.queue)==0):
            print("Queue is empty")
        else: 
            print("Queue is: ",end="")
            for i in self.queue:
                print(f"{i} | ",end="")
            print()

    def enqueue(self,item):
        self.queue.append(item)

    def dequeue(self):
        if(len(self.queue)==0):
            print("Queue is empty, cannot delete")
        else:
            front = self.queue[0]
            print("Deleting element:",front)
            self.queue=self.queue[1:]


q = Queue()

q.display()

q.enqueue(5)
q.enqueue(4)
q.enqueue(3)
q.display()

q.dequeue()
q.display()

q.dequeue()
q.dequeue()
q.display()

q.dequeue()

