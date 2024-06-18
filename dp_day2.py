'''ip:
    4x3
op:
    - - - -
    - - - -
    - - - -
print all possible paths from start to end'''
'''#value in the top and left as 1(3,3)->4(1+1)*2
  1 2 3 4
1 1 1 1 1 
2 1 1 1 4
3 1 1 4 
4 1 1

1 2  3  4
5 6  7  8
9 10 11 12
d={1:[2,5],2:[1,6,3],3:'''


'''def fun(i,j,c):
    if(i<0 or i>=n or j<0 or j>=m):
        return c
    if(i==n-1 and j==m-1):
        c=c+1
        return c
    v.append((i,j))
    if((i-1,j) not in v):
        c=fun(i-1,j,c)
    if((i,j-1) not in v):
        c=fun(i,j-1,c)
    if((i+1,j) not in v):
        c=fun(i+1,j,c)
    if((i,j+1) not in v):
        c=fun(i,j+1,c)
    v.pop()
    return c    
n=int(input())
m=int(input())
v=[]
print(fun(0,0,0))'''


#for obstacles-k,l
def fun(i,j,c):
    if(i<0 or i>=n or j<0 or j>=m or (i==k and j==l)):
        return c
    if(i==n-1 and j==m-1):
        c=c+1
        return c
    v.append((i,j))
    if((i-1,j) not in v):
        c=fun(i-1,j,c)
    if((i,j-1) not in v):
        c=fun(i,j-1,c)
    if((i+1,j) not in v):
        c=fun(i+1,j,c)
    if((i,j+1) not in v):
        c=fun(i,j+1,c)
    v.pop()
    return c    
n=int(input())
m=int(input())
k=int(input())
l=int(input())
v=[]
print(fun(0,0,0))


#N-QUEEN
