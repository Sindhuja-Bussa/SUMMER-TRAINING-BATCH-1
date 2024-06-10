'''l=list(map(int,input().split()))
s1=[]
s2=[]
o=[]
for i in l:
    if i not in s1:
        s1.append(i)
    else:
        s2.append(i)
s3=[]
s4=[]
for i in s2:
    if i not in s3:
        s3.append(i)
    else:
        s4.append(i)
print([s1,s3,s4])'''
def duplicates(n,m):
    a=[]
    b=[]
    if len(n)==0:
        return m
    else:
        for i in n:
            if i not in b:
                b.append(i)
            else:
                a.append(i)
    m.append(b)
    return duplicates(a,m)
n=list(map(int,input().split()))
m=[]
print(duplicates(n,m))
'''l=list(map(int,input().split()))
m=[]
c=0
while(c!=len(a)):
    r=[]
    for i in range(len(a)):
        if(i not in a[i].isalpha()):
            if(a[i] not in r):
                c=c+1
                r.append(a[i])
                a[i]='a'
m.append(r)'''



'''l=list(map(int,input().split()))
d={}
m=[]
c=0
for i in l:
    
while(c!=len(a)):
    r=[]
    for i in range(len(a)):
        if(i not in a[i].isalpha()):
            if(a[i] not in r):
                c=c+1
                r.append(a[i])
                a[i]='a'
m.append(r)

































'''class node:
    def __init__(self,key):
        self.key=key
        self.lchild=None
        self.rchild=None
    def insert(self,data):
        if self.key == None:
            self.key=data
            return
        if self.key == data:
            return
        if data < self.key:
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild=node(data)
        else:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild=node(data)
    def search(self,data):
        if self.key==data:
            print("Node is found")
            return
        if data < self.key:
            if self.lchild:
                self.lchild.search(data)
            else:
                print("Node is not present in tree")
        else: 
            if self.rchild:
                self.rchild.search(data)
            else:
                print("Node is not present in tree")       
    def preorder(self):
        print(self.key,end=" ")
        if self.lchild:
            self.lchild.preorder()
        if self.rchild:
            self.rchild.preorder()
    def inorder(self):
        if self.lchild:
            self.lchild.inorder()
        print(self.key,end=" ")
        if self.rchild:
            self.rchild.inorder()
    def postorder(self):
        if self.lchild:
            self.lchild.postorder()
        if self.rchild:
            self.rchild.postorder()
        print(self.key,end=" ")
    def delete(self, data):
        if self.key==None:
            print("Tree is empty")
            return
        if data < self.key: 
            if self.lchild:
                self.lchild = self.lchild.delete(data)
            else:
                print("Node is not prsent in the tree")
        elif data > self.key :
            if self.rchild:
                self.rchild = self.rchild.delete(data)
            else:
                print("Node is not present in the tree")
        else:
            if self.lchild==None :
                temp=self.rchild
                self=None
                return temp
            if self.rchild==None:
                temp=self.lchild
                self=None
                return temp
            node=self.rchild
            while node.lchild:
                node=node.lchild
            self.key=node.key
            self.rchild = self.rchild.delete(node.key)
        return self
    def min(self):
        t=self
        while t.lchild:
            t=t.lchild
        print("Min Node:",t.key)
    def min_r(self):
        if self.lchild:
            self.lchild.min_r()
        elif self.lchild==None:
            print("Min Node Recursion:",self.key)
    def max(self):
        t=self
        while t.rchild:
            t=t.rchild
        print("Max Node:",t.key)
    def max_r(self):
        if self.rchild:
            self.rchild.max_r()
        elif self.rchild==None:
            print("Max Node Recursion:",self.key)
    def leaf(self):
        # base case

        if not self.key:
            return
        # implement iterative preorder traversal and start
        # storing leaf nodes.
        st = []
        st.append(self.key)
        while len(st) > 0:
            self.key = st.pop()
     
            # if node is leafnode, print its data
            if not self.key.lchild and not self.key.rchild:
                print(self.key.data, end=" ")
     
            if self.key.rchild:
                st.append(self.key.rchild)
            if self.key.lchild:
                st.append(self.key.lchild)
            
root=node(10)
l=[6,3,1,6,98,3,7]
for i in l:
    root.insert(i)
root.search(6)
print()
print("Pre Order Traversal")
root.preorder()
print()
print("In Order Traversal")
root.inorder()
print()
print("Post Order Traversal")
root.postorder()
print()
print("After Deleting 10")
root.delete(10)
root.inorder()
print()
root.min()
root.min_r()
root.max()
root.max_r()
root.sum()'''
