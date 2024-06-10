'''#alphabets

s=input()
b=""
c=0
for i in s:
    if i not in b:
        b=b+i
        c=c+1
if(c==27):
    print("yes")
else:
    print("no")
print(b)'''

#including special characters=input()
s=input()
a='abcdefghijklmnopqrstuvwxyz'
b=""
c=0
for i in s:
    if i  not in b:
        b=b+i
for i in b:
    if i in a:
        c=c+1
if(c==26):
    print("yes")
else:
    print("no")


a=input()
d={}
for i in a:
    if(i.islower()):
        d[i]=1
print(d)

a=input()
d=set()
for i in a:
    if(i.islower()):
        d.add(i)
print(d)


a=input()
d=[0]*26  [00000000000000...26's zeros]
for i in a:
    if(i.islower()):
        d[ord(i)-97]=1
print(d)

#count
a=input()
d=[0]*26  [00000000000000...26's zeros]
for i in a:
    if(i.islower()):
        d[ord(i)-97]+=1
print(d)
           
a=input()
d=[0]*26  [00000000000000...26's zeros]
for i in a:
    if(i.islower()):
        d[ord(i)-97]+=1
print(all(d))


a=[6,7,8,9,0]
print(all(a))#one zero false
