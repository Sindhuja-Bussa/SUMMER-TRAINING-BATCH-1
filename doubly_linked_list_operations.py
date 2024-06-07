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

        '''#method 2
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
        self.tail=t1'''

    def swap_2(self):
        t=self.head
        t1=self.head.nxt
        t3=None
        while(t!=None and t1.nxt!=None):
            if(t==self.head):
                t.nxt=t1.nxt
                t1.nxt=t
                t1.prev=t3
                t.prev=t1
                head=t1
                t,t1=t1,t
                t3=t1
            else:
                t.nxt=t1.nxt
                t1.nxt=t
                t1.prev=t3
                t.prev=t1
                t3.nxt=t1
                t,t1=t1,t
                t3=t1
            t=t.nxt.nxt
            t1=t1.nxt.nxt
        self.print()
    def balancedparenthesis(self,):
        t=self.head
        st=[]
        f=0
        while(t!=None ):
            if t.data=='(' or t.data=='{' or t.data=='[':
                st.append(t.data)
            else:
                if not st:
                    f=0
                if t.data==']' and st[-1]=='[':
                    st.pop()
                elif t.data==')' and st[-1]=='(':
                    st.pop()
                elif t.data=='}' and st[-1]=='{':
                    st.pop()
                else:
                    f=0
            t=t.nxt
        if not st:
            f=1
        else:
            f=0
        
        if(f==0):
            print("no")
        else:
            print("yes")

    def missing_paranthesis(self):
        t=self.head
        st=[]
        f=0
        c=0
        while(t!=None):
            if t.data=='(' or t.data=='[' or t.data=='{' :
                st.append(t.data)
                c=c+1
            else:
                if not st:
                    f=0
                if ((t.data==']' and st[-1]=='[') or (t.data=='}' and st[-1]=='{') or (t.data==')' and st[-1]=='(')):
                     st.pop()
                     c=c-1
                else:
                    c=c+1
                    break
            if not st:
                f=1
            else:
                f=0
            t=t.nxt
        if f==0:
            print('not valid')
        else:
            print('valid')
        print(c)

    def evod(self,t,es,os):
        if(t==None):
            return abs(es-os)
        if(t.data%2==0):
            es=es+t.data
        else:
            os=os+t.data
        return self.evod(t.nxt,es,os)
        self.print()
        
    def prime_count(self,t,c):
        if(t==None):
            return c
        def pnp(i,n):
            if(i>=(n//2)+1):
                return 1
            if(n%i==0):
                return 0
            return pnp(i+1,n)
        if(pnp(2,t.data)):
            c=c+1
        return self.prime_count(t.nxt,c)
        self.print()
             
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
'''dll1=Doubly_linkedlist()'''
dll.add_begin(3)
dll.add_begin(5)
dll.add_begin(7)
dll.add_begin(8)
dll.add_begin(9)
dll.add_begin(10)
dll.add_begin(12)
dll.add_begin(15)
'''dll.print()
dll.rev_print()
dll.search(20)
dll.search(50)
dll.leven_lodd()
dll.palindrome()
dll.print()
dll.swap_2()
dll.print()
n=input()
for i in n:
    dll1.add_end(i)
dll1.balancedparenthesis()
dll1.missing_paranthesis()'''
#dll1.print()
dll.print()
p=dll.evod(dll.head,0,0)
print(p)
s=dll.prime_count(dll.head,0)
print(s)



