#for input 1
n=int(input())
order=""
str=""
for i in range(n):
    order=input()
    str=input()
    for i in order:
        for j in str:
            if(i==j):
                print(j,end=" ")

n=int(input())
for i in range(n):
    order=input()
    str=input()
    for i in order:
        if j in str:
            x=str.count(j)
            print(x*j,end=" ")
    
    
n=int(input())
while(n):
    order=input()
    str=input()
    s=""
    for i in order:
        if(i in str):
            s=s+(i*str.count(i))
    print(s)
    n=n-1#stopping condition
