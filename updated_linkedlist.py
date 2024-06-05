'''class Node:
    def __init__(self,u):
        self.data=u
        self.ref=None
a=Node(10)
b=Node(20)
a.nxt=b
print(a.data,a.ref)
print(b.data,b.ref)'''

'''class Node:
    def __init__(self,u):
        self.data=u
        self.ref=None
head=Node(10)
head.ref=Node(20)
head.ref.ref=Node(30)
print(head.data)
print(head.ref.data)
print(head.ref.ref.data)'''
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      

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
                print(n.data,end="->")
                n=n.ref
    def sum(self):
        if(self.head==None):
            print("linked list is empty")
        else:
            s=0
            n=self.head
            while(n!=None):
                s=s+n.data
                n=n.ref
            print("\nSUM:",s)
    def add_end(self,data):
        new_node=Node(data)
        if(self.head==None):
            self.head=new_node
        else:
            n=self.head
            while(n.ref!=None):
                n=n.ref
            n.ref=new_node
    def add_even(self):
        if(self.head==None):
            print("linked list is empty")
        else:
            n=self.head
            s=0
            while(n!=None):
                if((n.data)%2==0):
                    s=s+n.data
                n=n.ref
            print("\nEVEN SUM:",s)
    def add_begin(self,data):
        new_node=Node(data)
        new_node.ref=self.head
        self.head=new_node
    def search(self,x):
        n=self.head
        flag=0
        while(n!=None):
            if(n.data==x):
                flag=1
                break
            n=n.ref
        if(flag==1):
            print("found")
        else:
            print("not found")
    def middle_node(self):
        slow_pointer=self.head
        fast_pointer=self.head
        while fast_pointer!=None and fast_pointer.ref!=None:
            fast_pointer=fast_pointer.ref.ref
            slow_pointer=slow_pointer.ref
        print("\nmiddle element:",slow_pointer.data)
    def possible_pairs(self):
        slow_pointer=self.head
        fast_pointer=self.head.ref
        while(slow_pointer.ref!=None):
            while(fast_pointer!=None):
                print(slow_pointer.data,",",fast_pointer.data)
                fast_pointer=fast_pointer.ref
            slow_pointer=slow_pointer.ref
            fast_pointer=slow_pointer.ref
    def leven_lodd(self):
        fast_pointer=self.head
        slow_pointer=self.head
        while(fast_pointer!=None and fast_pointer.ref!=None):
            slow_pointer=slow_pointer.ref
            fast_pointer=fast_pointer.ref.ref
        if(fast_pointer==None):
            print('even')
        else:
            print('odd')
    def sequence_count(self):
        c=1
        max=0
        n=self.head
        while(n.ref!=None):
            if(n.data+1==n.ref.data):
                c=c+1
                n=n.ref
                if(max<c):
                    max=c
            else:
                c=1
                n=n.ref
        print(max)
    def selection_sort(self):
        t1=self.head
        t2=self.head.ref
        while(t1.ref!=None):
            t2=t1.ref
            while(t2!=None):
                if(t1.data>t2.data):
                    t=Node(t1.data)
                    t1.data=t2.data
                    t2.data=t.data
                t2=t2.ref
            t1=t1.ref
        self.print()
    def bubble_sort(self):
        if self.head is None:
            return  # If the list is empty, there's nothing to sort
        
        N = self.head
        while N is not None:
            n = self.head
            while n.ref is not None:
                if n.data > n.ref.data:
                    # Swap the data of the nodes
                    temp = n.data
                    n.data = n.ref.data
                    n.ref.data = temp
                n = n.ref
            N = N.ref  # Move to the next node for the next pass
        
        self.print()

    ''''def bubble_sort(self): 
        N=self.head
        while(N!=None):
            n=self.head
            while(n.ref!=None):
                if(n.data>n.ref.data):
                    n.data=n.ref.data
                    n.ref.data=n.data
            N=N.ref
        self.print()
    def bubble_bestcase(self):
        c=0
        N=self.head
        p=None
        while(N.ref!=None):
            f=0
            n=self.head
            while(n.ref!=p):
                if(n.data>n.ref.data):
                    f=1
                    n.data,n.ref.data=n.ref.data,n.data
                n=n.ref
                c=c+1
            if(f==0):
                break
            return c
            p=n
            N=N.ref
        
        self.print()
    '''
    def bubble_bestcase(self):
        c = 0  # Counter to track the number of comparisons
        N = self.head  # Start from the head of the list
        p = None  # p is used to mark the end of the sorted section

        while N is not None and N.ref is not None:
            f = 0  # Flag to check if any swap happened in the current pass
            n = self.head  # Start from the head for each pass

            while n.ref != p:
                if n.data > n.ref.data:
                    f = 1  # Swap happened
                    n.data, n.ref.data = n.ref.data, n.data
                n = n.ref
                c += 1  # Increment comparison counter

            if f == 0:
                break  # If no swaps happened, the list is sorted

            p = n  # Move the boundary of the sorted section
            N = N.ref  # Move to the next node

        self.print()
        return c

    def reverse(self):
        if(self.head==None):
            printf("linked list is empty")
        else:
            prev=None
            cur=self.head
            nxt=self.head.ref
            while cur!=None:
                nxt=cur.ref
                #change the direction of the node
                cur.ref=prev
                #shifting the nodes
                prev=cur
                cur=nxt
            self.head=prev
            self.print()
            return self.head
        
LL=Linkedlist()
'''LL2=Linkedlist()
LL2.add_end(30)'''
LL.add_begin(9)
LL.add_begin(7)
LL.add_begin(6)
LL.add_begin(4)
LL.add_begin(2)
LL.add_begin(3)
LL.add_begin(1)
LL.add_begin(0)
LL.sum()
LL.add_even()
LL.search(20)
LL.search(30)
LL.print()
LL.middle_node()
LL.possible_pairs()
LL.leven_lodd()
LL.sequence_count()
LL.selection_sort()
print()
LL.bubble_sort()
print()
LL.bubble_bestcase()
print()
LL.reverse()
