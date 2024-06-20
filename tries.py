'''5 
1 word
2 word
True
3 wo
True
3 app
False'''

'''class node:
    def __init__(self):
        self.d={}
        self.flag=0
class tries:
    def __init__(self):
        self.root=node()
    def insert(self,str1):
        t=self.root
        for i in str1:#wa
            if i not in t.d:
                t.d[i]=node()#not there 
            t=t.d[i]#check for next iteration use temp varaible
        t.flag=1
    def word_search(self,str1):
        t=self.root
        for i in str1:
            if i not in t.d:
                return False
            t=t.d[i]
        if(t.flag==1):
            return True#when the word is completely found
        else:
            return False
    def prefix_search(self,str1):
        t=self.root
        for i in str1:
            if i not in t.d:
                return False
            t=t.d[i]
        return True
  t1=tries()'''#t1 is the object of class tries
'''t1.insert('word')
t1.insert('apple')'''
'''print(t1.word_search('word'))
print(t1.prefix_search('wo'))
print(t1.word_search('apple'))
print(t1.prefix_search('appl'))
print(t1.word_search('world'))
print(t1.prefix_list('wo'))
n=int(input())
for i in range(n):
    a,s=input().split()
    if(a=='1'):
        t1.insert(s)
    if(a=='2'):
        print(t1.word_search(s))
    if(a=='3'):
        print(t1.prefix_search(s))'''

class node:
    def __init__(self):
        self.d={}
        self.flag=0
class tries:
    def __init__(self):
        self.root=node()
    def insert(self,str1):
        t=self.root
        for i in str1:
            if i not in t.d:
                t.d[i]=node() 
            t=t.d[i]
        t.flag=1
    def word_search(self,str1):
        t=self.root
        for i in str1:
            if i not in t.d:
                return False
            t=t.d[i]
        if(t.flag==1):
            return True
        else:
            return False
    def prefix_search(self,str1):
        t=self.root
        for i in str1:
            if i not in t.d:
                return False
            t=t.d[i]
        return True
    def prefix_words(self,str1):
        def fun(t,s):
            if(t.flag==1):
                print(s)
            for i in t.d:
                fun(t.d[i],s+i)
        t=self.root
        s=""
        for i in str1:
            if i in t.d:
                s=s+i
                t=t.d[i]
            else:
                return
        fun(t,s)
    def prefix_count(self,str1):
        
    
    
t1=tries()
n=int(input())
for i in range(n):
    a,s=input().split()
    if(a=='1'):
        t1.insert(s)
    if(a=='2'):
        print(t1.word_search(s))
    if(a=='3'):
        print(t1.prefix_search(s))
    if(a=='4'):
        t1.prefix_words(s)
