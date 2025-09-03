class Node:
    def __init__(self,value):
        self.value=value 
        self.next=None
class LinkendList:
    def __init__(self):
        self.head=None
    def display(self):
        if self.head is None:
            return "list is empty"
        else:
            pointer=self.head
            while pointer:
                print(pointer.value, end="-->")
                pointer=pointer.next

    def ispresent(self,value):
         
        last=self.head
        while last is not None:
            if last.value==value:
                return True
            last=last.next
        return False

    def length(self):
        last=self.head
        counter=0
        while last is not None:
            counter+=1
            last=last.next
        
        return counter
    
    def append(self,value):
        
        if self.head is None:
            self.head=Node(value)
        else:
            last=self.head
            while last.next:
                last=last.next
            last.next=Node(value)
    
    def preppend(self,value):
        
        first_node=Node(value)
        first_node.next=self.head
        self.head=first_node

    def insert(self,value,index):
        
        if index==0:
            self.preppend(value)
        else:
            if self.head is None:
                raise ValueError("index is out of bound")
            else:
                last=self.head
                
                for i in range (index-1):
                    if last.next is None:
                        raise ValueError("index is out of bound")
                    last=last.next
                new_node=Node(value)
                new_node.next=last.next
                last.next=new_node
        
    def delete(self,value):
        last=self.head
        if last is not None:
            if last.value==value:
                self.head=last.next
            else:
                while last.next:
                    if last.next.value==value:
                        last.next=last.next.next
                        break

        
    def pop(self,index):
        if self.head is None:
            raise ValueError("index is out of bound")
        else:
            last=self.head
            for i in range (index-1):
                if last.next is None:
                    raise ValueError("index is out of bound")
                last=last.next
            if last.next is None:
                raise ValueError("index is out of bound")
            else:
                last.next=last.next.next

    
    def get(self,index):
        pass

# if __name__=="__main__":
obj=LinkendList()
obj.append(1)
obj.append(2)
# obj.display() 
obj.pop(1)
# obj.display()
obj.delete(2)
obj.display()



