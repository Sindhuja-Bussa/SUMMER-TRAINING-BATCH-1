'''n=list(map(int,input().split()))
l=[]
for i in n:
    l.append(i)
    l.sort(reverse=True)
print(l)
print(n)'''

def fun(l):
    if(len(l)==0):
        return 0
    if(len(l)==1):
        return l[0]
    if(len(l)==2):
        return max(l)
    le=l[0]+fun(l[2:])
    ri=l[1]+fun(l[3:])
    return max(le,ri)        
l=list(map(int,input().split()))
print(fun(l))

