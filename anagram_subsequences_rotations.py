'''ip:
    school
    3
    L 2 ->hoolsc
    R 3 ->oolsch
    L 1 ->chools

op:
    yes
hoc
sub:
    sch,cho,hoo,ool'''
s=input()
q=int(input())
l=[]
x=''
for i in range(q):
    l.append(input())
    l.append(int(input()))
print(l)
for j in range(0,len(l),2):
    if l[j]=='L':
        x=x+s[l[j+1]]
    elif l[j]=='R':
        x=x+s[l[-(j+1)]]
print(x)
x=list(x)
x.sort()
print(x)
#for i in range(len(s)-(q-1)):
 #   s1.append([s[i:q+i]])
#print(s1
s1=[]
for i in range(len(s)-(q-1)):
    t=list(s[i:q+i])
    t.sort()
    s1.append(t)
print(s1)
for i in s1:
    if i==x:
        print("yes")
        break
else:
    print("no")




