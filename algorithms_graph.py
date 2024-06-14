#Dijkstras Algorithm
def dijkstra(g,x):
    d={5:9999,7:9999,4:9999,8:9999,3:9999,2:9999}
    d[x]=0
    v=[]
    q=[x]
    while(q):
        m=9999
        for i in q:
            if(d[i]<m):
                m=d[i]
                x=i
        for i in g[x]:
            if(i[0] not in v and i[0] not in q):#[1,6,6] take min so no need to keep condition for q
                q.append(i[0])
                if d[i[0]]>i[1]+d[x]:
                    d[i[0]]=i[1]+d[x]
        
        v.append(x)
        q.remove(x) #q=[5,3,1,6] [3,1,6]
    return d
g={5:[(7,1),(3,2)],7:[(5,1),(4,3),(3,1)],4:[(7,3),(8,2),(2,3)],8:[(3,4),(4,2),(2,5)],3:[(5,2),(7,1),(8,4)],2:[(4,3),(8,5)]}
print(dijkstra(g,5))

