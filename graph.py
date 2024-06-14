'''#visited nodes
def fun(d,x):
    l.append(x)
    for i in d[x]:
        if i not in l:
            fun(d,i)
l=[]
d={5:[7,3],7:[5,4,3],4:[7,8,2],8:[3,4,2],3:[5,7,8],2:[4,8]}
fun(d,5)
print('visited nodes',l)



#all possible paths
def paths(d,x):
    l.append(x)
    if x==2:
        print(l)
        l.pop()
        return 
    for i in d[x]:
        if i not in l:
            paths(d,i)
        
    l.pop()
d={5:[7,3],7:[5,4,3],4:[7,8,2],8:[3,4,2],3:[5,7,8],2:[4,8]}
l=[]
paths(d,5)'''



'''def cost_path(d,x,c):
    l.append(x)
    if x==2:
        print(l,'-',c)
        l.pop()
        return c
    
    for i in d[x]:
        if i[0] not in l:
            #c=c+i[1]
            #print(i[0],i[1])
            cost_path(d,i[0],c+i[1])
    l.pop()        
          
    

d={5:[(7,1),(3,2)],7:[(5,1),(4,3),(3,1)],4:[(7,3),(8,2),(2,3)],8:[(3,4),(4,2),(2,5)],3:[(5,2),(7,1),(8,4)],2:[(4,3),(8,5)]}
l=[]
cost_path(d,5,0)'''
'''

#shortest cost
def short_cost(d,e,x,c,m):
    l.append(x)
    if x==e:
        if c<m:
            m=c
        l.pop()
        return m
    
    for i in d[x]:
        if i[0] not in l:
            #c=c+i[1]
            m=short_cost(d,e,i[0],c+i[1],m)
    l.pop()
    return m

d={5:[(7,1),(3,2)],7:[(5,1),(4,3),(3,1)],4:[(7,3),(8,2),(2,3)],8:[(3,4),(4,2),(2,5)],3:[(5,2),(7,1),(8,4)],2:[(4,3),(8,5)]}
l=[]
n=int(input())
n1=int(input())
print(short_cost(d,n1,n,0,99999999))


#shortest cost & path
def short_path(d,e,x,c,m,l1):
    l.append(x)
    if x==e:
        if c<m:
            m=c
            l1=l.copy()
        l.pop()
        return m,l1
    
    for i in d[x]:
        if i[0] not in l:
            #c=c+i[1]
            m,l1=short_path(d,e,i[0],c+i[1],m,l1)
    l.pop()
    return m,l1

d={5:[(7,1),(3,2)],7:[(5,1),(4,3),(3,1)],4:[(7,3),(8,2),(2,3)],8:[(3,4),(4,2),(2,5)],3:[(5,2),(7,1),(8,4)],2:[(4,3),(8,5)]}
l=[]
n=int(input())
n1=int(input())
print(short_path(d,n1,n,0,99999999,[]))


#print all paths from 5 to all nodes


def paths(d,x,e):
    l.append(x)
    if x==e:
        print(l)
        l.pop()
        return 
    for i in d[x]:
        if i not in l:
            paths(d,i,e)
        
    l.pop()
d={5:[7,3],7:[5,4,3],4:[7,8,2],8:[3,4,2],3:[5,7,8],2:[4,8]}
l=[]

for i in d:
    paths(d,5,i)



#shortest path from 5 to all nodes


def short_path(d,e,x,c,m,l1):
    l.append(x)2w2    if x==e:
        if c<m:
            m=c
            l1=l.copy()
        l.pop()
        return m,l1
    
    for i in d[x]:
        if i[0] not in l:
            #c=c+i[1]
            m,l1=short_path(d,e,i[0],c+i[1],m,l1)
    l.pop()
    return m,l1

d={5:[(7,1),(3,2)],7:[(5,1),(4,3),(3,1)],4:[(7,3),(8,2),(2,3)],8:[(3,4),(4,2),(2,5)],3:[(5,2),(7,1),(8,4)],2:[(4,3),(8,5)]}
l=[]
n=int(input())
for i in d:
    print(short_path(d,i,n,0,99999999,[]))'''


'''#Breadth First Search 
def bfs_visit(d,x):
    v=[]
    q=[x]
    while(q):
        for i in d[q[0]]:
            if i not in q and i not in v:
                q.append(i)
        #q.pop(0)to remove first element
        v.append(q.pop(0))
    print(v)
d={5:[7,3],7:[5,4,3],4:[7,8,2],8:[3,4,2],3:[5,7,8],2:[4,8]}
bfs_visit(d,5)

def bfs_costv(d,x):
    v=[]
    q=[x]
    while(q):
        for i in d[q[0]]:
            if i[0] not in q and i[0] not in v:
                q.append(i[0])
        #q.pop(0)to remove first element
        v.append(q.pop(0))
    print(v)
d={5:[(7,1),(3,2)],7:[(5,1),(4,3),(3,1)],4:[(7,3),(8,2),(2,3)],8:[(3,4),(4,2),(2,5)],3:[(5,2),(7,1),(8,4)],2:[(4,3),(8,5)]}
bfs_costv(d,5)'''







