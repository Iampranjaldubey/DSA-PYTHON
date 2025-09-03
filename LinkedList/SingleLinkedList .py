

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def insertAtFirst(self,data):
        print(f"Inserting node at first: {data}")
        nd = Node(data)
        nd.next = self.head
        self.head = nd
        self.size += 1

    def insertAtLast(self,data):
        nd = Node(data)
        if(self.size==0):
            self.insertAtFirst(data)
        else:
            print(f"Inserting node at last: {data}")
            currNode = self.head
            while(currNode.next):
                currNode = currNode.next
            currNode.next = nd
            self.size += 1
    def display(self):
        if(self.size==0):
            print("List is empty")
        else:
            print("List is: ",end="")
            currNode = self.head
            while(currNode):
                print(currNode.data," -> ",end="")
                currNode = currNode.next
            print(currNode)

    def InsertAtLocation(self,loc, data): # 2 -> 1 -> None 
        if(loc==0):
            self.insertAtFirst(data)
        elif(loc==self.size):
            self.insertAtLast(data)
        elif(loc>0 and loc<self.size):
            print("Inserting element at location: ",loc,"\t",data)
            count = 0
            nd = Node(data)
            currNode = self.head
            while(count<loc-1): # 2 -> 1 -> 3 -> 4 -> None loc=2
                currNode = currNode.next
                count += 1
            nd.next = currNode.next
            currNode.next = nd
            self.size += 1
        else:
            print("cannot insert at invalid location")

    def deleteFirst(self):
        if(self.size==0):
            print("cannot delete, list empty")
        else:
            print("Deleting element form last: ",self.head.data)
            self.head = self.head.next
            self.size -= 1

    def showSize(self):
        print("size of list: ",self.size)

    def deleteLast(self):
        if(self.size==0):
            print("cannot delete, list empty")
        elif(self.size==1):
            print("Deleting element form last: ",self.head.data)
            self.head = self.head.next
            self.size -= 1
        else:
            currNode = self.head
            while(currNode.next.next): # 2->1->3->None
                currNode = currNode.next
            print("deleting element from last: ",currNode.next.data)
            currNode.next = None
            self.size -= 1

    def deleteFromLocation(self,loc):
        if(self.size==0):
            print("cannot delete, list empty")
        elif(loc==0):
            self.deleteFirst()
        elif(loc==(self.size-1)):
            self.deleteLast()
        elif(loc>0 and loc<(self.size-1)):# 2 -> 1 -> 3 -> 4 -> None loc=2
            count = 0
            currNode = self.head
            while(count<loc-1):
                currNode = currNode.next
                count += 1
            print("deleting element form location",loc,"\t",currNode.next.data)
            currNode.next = currNode.next.next
            self.size -= 1
        else:
            print("cannot delete from invalid location")



ll=LinkedList()
ll.display()
ll.deleteFromLocation(0)

ll.insertAtLast(1)
ll.insertAtFirst(2)
ll.deleteFromLocation(1)
ll.deleteFromLocation(0)
ll.display()

ll.InsertAtLocation(0,3)
ll.display()

ll.InsertAtLocation(3,4)
ll.display()

ll.InsertAtLocation(2,5)
ll.display()

ll.insertAtFirst(12)
ll.insertAtFirst(21)
ll.insertAtFirst(20)
ll.insertAtFirst(23)
ll.insertAtFirst(25)
ll.insertAtFirst(26)
ll.display()

ll.deleteLast()
ll.display()

ll.deleteFromLocation(2)
ll.display()

ll.deleteFromLocation(4)
ll.display()

ll.showSize()
