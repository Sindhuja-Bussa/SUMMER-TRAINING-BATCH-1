class Node:
    def __init__(self,data):
        self.data=data
        self.nxt=None
        self.prev=None
class Doubly_linkedlist:
    def __init__(self):
        self.head=None
        self.tail=None
    def print(self):
        n=self.head
        while(n!=None):
            print(n.data,end="->")
            n=n.nxt
        print()
    def add_begin(self,data):
        new_node = Node(data)
        if(self.head==None):
            self.head = new_node
            self.tail=self.head
        else:
            new_node.nxt = self.head
            self.head.prev = new_node
            self.head = new_node
    def add_end(self,data):
        new_node = Node(data)
        if(self.head==None):
            self.head = new_node
            self.tail=self.head   
        else:
            new_node.prev = self.tail
            self.tail.nxt = new_node
            self.tail = new_node
    def rev_print(self):
        t=self.tail
        while(t!=None):
            print(t.data,end="->")
            t=t.prev
        print()
        
    def add_after(self,data,x):
        if self.head is None:
            print("LL is empty!")
        else:
            n =self.head
            while n is not None:
                if x==n.data:
                    break
                n = n.nxt
            if n is None:
                print("Given Node is not present in DLL")
            else:
                new_node = Node(data)
                new_node.nxt = n.nxt
                new_node.prev = n
                if n.nxt is not None:
                    n.nxt.prev = new_node
                n.nxt = new_node
                
    def add_before(self,data,x):
        if self.head is None:
            print("LL is empty!")
        else:
            n = self.head
            while n is not None:
                if x==n.data:
                    break
                n = n.nxt
            if n is None:
                print("Given Node is not present in DLL")
            else:
                new_node = Node(data)
                new_node.nxt = n
                new_node.prev = n.prev               
                if n.prev is not None:
                    n.prev.nxt = new_node
                else:
                    self.head = new_node
                n.prev = new_node
    def delete_begin(self):
        if self.head is None:
            print("DLL is empty can't delte !")
            return
        else:
            self.head = self.head.nxt
            self.head.prev = None
    def delete_end(self):
        if self.head is None:
            print("DLL is empty can't delte !")
            return
        else:
            self.tail = self.tail.prev
            self.tail.nxt = None
    def delete_by_value(self,x):
        if self.head is None:
            print("DLL is empty can't delte !")
            return
        if self.head.nxt is None:#if it is only one node
            if x==self.head.data:
                self.head = None
            else:
                print("x is not present in DLL")
        if self.head.data == x: #if it is first node
            self.head = self.head.nxt
            self.head.prev = None
            return
        n = self.head
        while n.nxt is not None:
            if x==n.data:
                break
            n = n.nxt
        if n.nref is not None:#middle nodes
            n.nref.pref = n.pref
            n.pref.nref = n.nref
        else:#last node
            if n.data==x:
                n.pref.nref = None
            else:
                print("x is not present in dll!")

dll=Doubly_linkedlist()
dll.add_end(40)
dll.add_begin(20)
dll.add_begin(30)
dll.add_begin(50)
dll.print()
dll.delete_by_value(20)
dll.print()
