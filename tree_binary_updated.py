class node:
  def __init__(self,n):
    self.data=n
    self.left=None
    self.right=None
class tree:
    def __init__(self):
        self.root=None
    def creat(self,root,x):
        if self.root==None:
            self.root=node(x)
            return self.root
        if root==None:
            return node(x)
        elif(root.data>x):
            root.left=self.creat(root.left,x)
        else:
            root.right=self.creat(root.right,x)
        return root
    def preorder(self,root):
        if root:
            print(root.data,end=" ")
            self.preorder(root.left)
            self.preorder(root.right)
    def inorder(self,root):
        if root:
            self.inorder(root.left)
            print(root.data,end=" ")
            self.inorder(root.right)
    def postorder(self,root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data,end=" ")
    def sum(self,root,s):
        #preorder traversal
        if root:
            s = s+ root.data + self.sum(root.left,s)+self.sum(root.right,s)
        #inorder traversal
        #if root:
           # s = s+ self.sum(root.left,s)+ root.data +self.sum(root.right,s)
            #without passing s
            #without passing s
        #if root:
            #return root.data + self.sum(root.left)+self.sum(root.right)
        #else:
            #return 0
           
        return s   
    def even_sum(self,root,es):
        if root:
            if((root.data)%2==0):
                es = es + root.data + self.even_sum(root.left,es)+self.even_sum(root.right,es)
            else:
                es = es + self.even_sum(root.left,es)+self.even_sum(root.right,es)
        return es
    def odd_sum(self,root,os):
        if root:
            if((root.data)%2!=0):
                os = os + root.data + self.odd_sum(root.left,os)+self.odd_sum(root.right,os)
            else:
                os = os + self.odd_sum(root.left,os)+self.odd_sum(root.right,os)
        return os
    def abs_diff_esum_osum(self,root):
        x=self.even_sum(t1.root,0)
        y=self.odd_sum(t1.root,0)
        return abs(x-y)
    def abs_diff_esum_osum_1(self,root,es,os):
        if root:
            if((root.data)%2==0):
                es = es + root.data + self.even_sum(root.left,es)+self.even_sum(root.right,es)
            else:
                es = es + self.even_sum(root.left,es)+self.even_sum(root.right,es)
            if((root.data)%2!=0):
                os = os + root.data + self.odd_sum(root.left,os)+self.odd_sum(root.right,os)
            else:
                os = os + self.odd_sum(root.left,os)+self.odd_sum(root.right,os)
        return abs(es-os)
    def abs_diff_esum_osum_2(self,root):
        if root:
            if((root.data)%2==0):
                return root.data + self.abs_diff_esum_osum_2(root.left)+self.abs_diff_esum_osum_2(root.right)
            return -root.data+self.abs_diff_esum_osum_2(root.left)+self.abs_diff_esum_osum_2(root.right)
        else:
            return 0
    def height(self,root):
        if root==None:
            return -1
        return max(self.height(root.left),self.height(root.right))+1
    def balanced(self,root):
        return abs(self.height(root.left)-self.height(root.right)) <= 1
        if(balanced(self.root)):
            print("Balanced Tree")
        else:
            print("Not Balanced")
    def c_leaf_nodes(self,root):
        if root==None:
            return 0
        if(root.left==None and root.right==None):
            return 1
        return (self.c_leaf_nodes(root.left)+self.c_leaf_nodes(root.right))
    def s_leaf_nodes(self,root):
        if root==None:
            return 0
        if root:
            if(root.left==None and root.right==None):
                return root.data+self.s_leaf_nodes(root.left)+self.s_leaf_nodes(root.right)
            return self.s_leaf_nodes(root.left)+self.s_leaf_nodes(root.right)
    def search(self,root,x):
        if root==None:
            return 0
        if(root.data==x):
          return 1
        elif(root.data>x):
          return self.search(root.left,x)
        else:
          return self.search(root.right,x)
    def depth(self,root,x,c):
        if root==None:
            return -1
        if(root.data==x):
            return c
        if(root.data>x):
            return self.depth(root.left,x,c+1)
        else:
            return self.depth(root.right,x,c+1)
    def left_view(self,root,c,l):
      if root==None:
        return
      if c not in l:
        l.append(c)
        print(root.data,end=" ") 
      self.left_view(root.left,c+1,l)
      self.left_view(root.right,c+1,l)

    def right_view(self,root,c,l):
      if root==None:
        return
      if c not in l:
        l.append(c)
        print(root.data,end=" ") 
      self.right_view(root.right,c+1,l)
      self.right_view(root.left,c+1,l)
    def top_view(self,root,c,d):
      if root==None:
        return
      if c not in d:
        d[c]=root.data
        #print(root.data)
      self.top_view(root.left,c+1,d)
      self.top_view(root.right,c-1,d)
      return sorted(d.values())
    def bottom_view(self,root,c,d):
      if root==None:
        return
      if(c not in d and :
        d[c]=root.data
        #print(root.data)
      self.top_view(root.left,c+1,d)
      self.top_view(root.right,c-1,d)
      return sorted(d.values())
    
t1=tree()
#t1.root=node(10)
t1.creat(t1.root,10)
t1.creat(t1.root,5)
t1.creat(t1.root,2)
t1.creat(t1.root,7)
t1.creat(t1.root,15)
t1.creat(t1.root,11)
t1.creat(t1.root,20)
t1.creat(t1.root,21)
t1.creat(t1.root,22)
print("Preorder")
t1.preorder(t1.root)
print()
print("Inorder")
t1.inorder(t1.root)
print()
print("Postorder")
t1.postorder(t1.root)
print()
print("Sum:",t1.sum(t1.root,0))
print("Left Sum:",t1.sum(t1.root.left,0))
print("Abs Diff Left & Right Sum:",abs(t1.sum(t1.root.left,0)-t1.sum(t1.root.right,0)))
print("Right Sum:",t1.sum(t1.root.right,0))
print("Even Sum:",t1.even_sum(t1.root,0))
print("Odd Sum:",t1.odd_sum(t1.root,0))
print("Abs Diff Even & Odd Sum:",t1.abs_diff_esum_osum(t1.root))
print("Abs Diff Even & Odd Sum_Method_2:",t1.abs_diff_esum_osum_1(t1.root,0,0))
print("Abs Diff Even & Odd Sum_Method_3:",t1.abs_diff_esum_osum_2(t1.root))
print("Height of Tree:",t1.height(t1.root))
print("Balanced Tree:",t1.balanced(t1.root))
print("No.of Leaf Nodes:",t1.c_leaf_nodes(t1.root))
print("Sum of Leaf Nodes:",t1.s_leaf_nodes(t1.root))
t1.search(t1.root,23)
print("Depth of Tree:",t1.depth(t1.root,8,0))
print("Left View")
t1.left_view(t1.root,0,[])
print()
print("Right View")
t1.right_view(t1.root,0,[])
print()
print("Top View")
print(t1.top_view(t1.root,0,{}))
print()
print("Bottom View")
print(t1.top_view(t1.root,0,{}))

