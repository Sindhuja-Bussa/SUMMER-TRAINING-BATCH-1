class node:
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
    def delete(self,data):
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
    def sum(self):
        total = self.sum_r()
        print("Sum of all nodes:", total)
    
    def sum_r(self):
        total=self.key
        if self.lchild:
            total=total+self.lchild.sum_r()
        if self.rchild:
            total=total+self.rchild.sum_r()
        return total
    def even_sum(self):
        res = self.even_sum_r()
        print("Sum of even nodes:",res)
    def even_sum_r(self):
        s=0
        if self.key % 2 == 0 :
            s=s+self.key
        if self.lchild:
            s += self.lchild.even_sum_r()
        if self.rchild:
            s += self.rchild.even_sum_r()
        return s
    def odd_sum(self):
        res = self.odd_sum_r()
        print("Sum of odd nodes:",res)
    def odd_sum_r(self):
        s=0
        if self.key % 2 != 0 :
            s=s+self.key
        if self.lchild:
            s += self.lchild.odd_sum_r()
        if self.rchild:
            s += self.rchild.odd_sum_r()
        return s
    def abs_diff_EvenOdd(self):
        even_sum=self.even_sum_r()
        odd_sum=self.odd_sum_r()
        abs_diff=abs((even_sum) - (odd_sum))
        print("Absolute Difference EvenOdd:",abs_diff)
    def leaf_nodes(self):
        if self.lchild==None and self.rchild==None:
            print(self.key, end=" ")
        if self.lchild:
            self.lchild.leaf_nodes()
        if self.rchild:
            self.rchild.leaf_nodes()
root=node(None)
l=[10,5,2,1,6,8,9]
for i in l:
    root.insert(i)
root.search(6)
print("Pre Order Traversal")
root.preorder()
print()
print("In Order Traversal")
root.inorder()
print()
print("Post Order Traversal")
root.postorder()
print()
print("After Deleting 5")
root.delete(5)
root.inorder()
print()
root.min()
root.min_r()
root.max()
root.max_r()
root.sum()
root.even_sum()
root.odd_sum()
root.abs_diff_EvenOdd()
print("Leaf Nodes:")
root.leaf_nodes()
