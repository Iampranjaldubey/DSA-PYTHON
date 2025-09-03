class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class CircularList:
    def __init__(self):
        self.head = None
        self.size = 0

    def showSize(self):
        print("size of list: ",self.size)

    def insertAtFirst(self,data):
        nd = Node(data)
        print("inserting element at first: ",nd.data)
        if(self.size==0):
            self.head = nd
            nd.next = self.head
        else: # 0 -> 1 -> 2 -> 3 -> 4 -> 0   0.next = head head = 0
            nd.next = self.head
            self.head = nd
            currNode = self.head
            count = 0
            while(count<self.size): # c= 4, size = 4  0 -> 1 -> 2 -> 3 -> 4 -> None
                count += 1
                currNode = currNode.next
            currNode.next = nd
        self.size += 1

    def display(self):
        if(self.size==0):
            print("list is empty")
        else:
            print("List is: ",end="")
            currNode = self.head # 2 -> 1 -> 2
            count = 0
            while(count<self.size): #c=5, s=5      5 -> 4 -> 3 -> 2 -> 1 -> 5
                count += 1
                print(f"{currNode.data} -> ",end="")
                currNode = currNode.next
            print(currNode.data)


cll = CircularList()
cll.insertAtFirst(1)
cll.insertAtFirst(2)
cll.insertAtFirst(3)
cll.display()

cll.insertAtFirst(4)
cll.insertAtFirst(5)
cll.display()
cll.showSize()


## Task: Implement Doubly Linked List
