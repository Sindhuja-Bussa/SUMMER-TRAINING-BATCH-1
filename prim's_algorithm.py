#Prim's Algorithm
d={5:[(2,2),(3,2),(8,2)],2:[(3,1),(5,2)],3:[(2,1),(5,2),(8,2),(7,3)],8:[(5,2),(3,3),(6,4)],6:[(8,4),(9,2)],7:[(3,3),(9,1)],9:[(6,2),(7,1),(4,2)],4:[(9,2)]}
def fun(q):
    return q[2]
def prims(i,c,v):
     q=[]
     for j,k in d[i]:
         q.append((i,j,k))
     v.append(i)
     l=[]
     while q:
        q.sort(key=fun)
        if q[0][1] not in v:
         l.append(q[0])
         v.append(q[0][1])
         for i,j in d[q[0][1]]:
            if i not in v:
                q.append((q[0][1],i,j))
        q.pop(0)
         
     print(l)
i=list(d.keys())[0]
prims(i,0,[])
