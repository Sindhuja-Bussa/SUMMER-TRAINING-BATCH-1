'''ip:
    6
    0 1 1 1 0 1
    0 1 0 1 0 0
    1 0 1 1 0 0
    0 0 0 1 1 1
    1 1 0 0 0 1
    1 1 1 0 1 0
    4 6#
    op : 8
def fun(i,j):
    if i<0 or i>len(l)-1 or j<0 or j >len(l)-1:
        return
    if l[i][j]==0:
        return 
    else:
        if l[i][j]==1:
            l[i][j]=0
        fun(i-1,j)
        fun(i,j-1)
        fun(i+1,j)
        fun(i,j+1)
    return        
n=int(input())  
l=[]
for i in range(n):
    a=[]
    for j in range(n):
        a.append(int(input()))
    l.append(a)
r=int(input())
c=int(input())
fun(r-1,c-1)#to start from 0
c=0
for i in range(len(l)):
    for j in range(len(l)):
        if l[i][j]==1:
            c=c+1
print(l)
print(c)'''







