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
        t=self.head
        while(t!=None):
            print(t.data,end="->")
            t=t.nxt
        print()
    def add_end(self,data):
        if(self.head==None):
            self.head=Node(data)
            self.tail=self.head
        else:
            t=Node(data)
            self.tail.nxt=t
            t.prev=self.tail
            self.tail=self.tail.nxt
    def add_begin(self,data):
        if(self.head==None):
            self.head=Node(data)
            self.tail=self.head
        else:
            t=Node(data)
            self.head.prev=t
            t.nxt=self.head
            self.head=self.head.prev
    def rev_print(self):
        t=self.tail
        while(t!=None):
            print(t.data,end="->")
            t=t.prev
        print()
    '''def search(self,x):
        t=self.head
        flag=0
        while(t!=None):
            if(t.data==x):
                flag=1
                break
            t=t.nxt
        if(flag==1):
            print("found")
        else:
            print("not found")'''
    def search(self,x):
        t=self.head
        s=self.tail
        flag=0
        while(t!=None and s!=None):
            if(t.data==x or s.data==x):
                flag=1
                break
            t=t.nxt
            s=s.prev
        if(flag==1):
            print("found")
        else:
            print("not found")
    def leven_lodd(self):
        t=self.head
        s=self.tail
        while(t!=s and t!=s.nxt):
            t=t.nxt
            s=s.prev
        if(t==s):
            print('odd')
        else:
            print('even')
    def palindrome(self):
        t=self.head
        s=self.tail
        flag=0
        while(t!=s and t!=s.nxt):
            if(t.data==s.data):
                flag=1
            else:
                flag=0
                break
            t=t.nxt
            s=s.prev
        if(flag==1):
            print("palindrome")
        else:
            print("not palindrome")
    def swap(self):
        t=self.head
        s=self.tail
        while(t.nxt!=s):
            t=t.nxt
            s=s.prev
        t=self.head
        while(s!=None):
            temp=Node(t.data)#3
            t.data=s.data
            s.data=temp.data
            t=t.nxt
            s=s.nxt
        self.print() 

        #method 2
       fast=self.head
        slow=self.head
        while(fast!=None):
            fast=fast.next.next
            slow=slow.next
        self.tail.next=self.head
        self.head.prev=self.tail
        t1=self.prev
        t1.next=None
        slow.prev=None
        self.head=slow
        self.tail=t1  
    '''def search(self,x):
        t=self.head
        s=self.tail
        flag=0
        while(t!=s and t!=s.next):
            if(t.data==x or s.data==x):
                return 1
            t=t.nxt
            s=s.prev
        for odd'
        if(t.data==x):
            return 1
        else:
            return 0'''
    
dll=Doubly_linkedlist()
dll.add_begin(3)
dll.add_begin(5)
dll.add_begin(7)
dll.add_begin(8)
dll.add_begin(9)
dll.add_begin(10)
dll.add_begin(12)
dll.add_begin(15)
dll.print()
dll.rev_print()
dll.search(20)
dll.search(50)
dll.leven_lodd()
dll.palindrome()
dll.print()
dll.swap()

