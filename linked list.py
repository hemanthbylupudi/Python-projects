class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist():
    def __init__(self):
        self.head=None
    def insert(self,data):
        newNode=node(data)
        if self.head is None:
            self.head=newNode
        else:
            newNode.next=self.head
            self.head=newNode
    def display(self):
        current=self.head
        while current:
            print(current.data)
            current=current.next
    def search(self,key):
        self.key=key
        count=0
        current=self.head
        while current:
            count +=1
            if current.data==self.key:
                print("{} found at {}".format(key,count))
                break
            else:
                current=current.next
    def delete(self,key):
        self.key=key
        current=self.head
        while current:
            if current.data==key:
                
            
obj=linkedlist()
obj.insert(7)
obj.insert(8)
obj.insert(10)
obj.insert(11)
obj.display()
obj.search(7)





