'''ip:
    3
    xyz
    pqr
    abc
    "yraxpbzq"
op:
    no
m[i]=m[i].replace(i,' ')
it replaces everything entire row
string is inmutable
it will not replace
so, list(input())'''

'''n=int(input())
m = []
for i in range(n):
    for j in range(n):
        m.append(list(input()))  
str=input()
index=0
flag=0
for i in str:
    if i in m[index]:
        flag=1
        index=index+1
        if(index==n):
            index=0
    else:
        flag=0
        break
if(flag==0):
    print("no")
else:
    print("yes")'''
        
'''for i in range(len(str)):
    if i in m[i%n]:
        continue
    else:
        f=1
        break
if(flag==0):
    print("no")
else:
    print("yes")       
        
for i in range(len(str)):
    if str[i] not in m[i%n]:
        print("no")
        break
else:
    print("yes")'''
"""//for repeating elements"""
n=int(input())
m = []
for i in range(n):
        m.append(list(input()))  
str=input()
f=0
for i in range(len(str)):
    if(str[i] not in m[i%n]):
        print("no")
        f=1
        break
    else:
        m[i%n].remove(str[i])
if(f==0):
    print("yes")
    
'''f=True
n=int(input())
m = []

s=input()
sl=len(s)
for i in range(sl):
    if s[i] in m[i%n]:
        m[i%n].remove(s[i])
    else:
        f=False
print(f)        
ip:
     [4,7,1,4,1,3]
     3
     5
op:
    2'''
