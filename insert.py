class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None

class Linkedlist:
    def __init__(self):
        self.head=None
    def print(self):
        if(self.head==None):
            print("linked list is empty")
        else:
            n=self.head
            while(n!=None):
                print(n.data,"-->",end=" ")
                n=n.ref
    def add_begin(self,data):
        new_node=Node(data)
        new_node.ref=self.head
        self.head=new_node
    def add_end(self,data):
        new_node=Node(data)
        if(self.head==None):
            self.head=new_node
        else:
            n=self.head
            while(n.ref!=None):
                n=n.ref
            n.ref=new_node
    def add_after(self,data,x):
        n=self.head
        while(n!=None):
            if(n.data==x):
                break
            n=n.ref
        if(n==None):
            print("Node is not found")
        else:
            new_node=Node(data)
            new_node.ref=n.ref
            n.ref=new_node    
    def add_before(self,data,x):
        if(self.head==None):
            print("linked list is empty")
            return
        if(self.head.data==x):
            new_node=Node(data)
            new_node.ref=self.head
            self.head=new_node
            return
        n=self.head
        while(n.ref!=None):
            if(n.ref.data==x):
                break
            n=n.ref
        if(n.ref==None):
            print("Node is not found")
        else:
            new_node=Node(data)
            new_node=n.ref
            n.ref=new_node           
LL=Linkedlist()
LL.add_end(30)
LL.add_begin(20)
LL.add_end(40)
LL.add_before(10,20)
LL.add_after(45,40)
LL.print()
                
        
        
    
    
    
    
