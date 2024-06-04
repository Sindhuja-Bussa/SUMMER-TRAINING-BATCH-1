'''prime numbers
ip:
    13           14
op:
    13           17
[[[[to print prime or not
n=int(input())
count=0
for i in range(1,n+1):
    if(n%i==0):
        count=count+1
if count==2:
    print("prime")
else:
    print("not prime")
]]]]

[[[for output method 1

def prime(n):
    count=0
    for i in range(2,(n//2)+1):
        if(n%i==0):
            count=count+1
    if count==0:
        return True
    else:
        return False
n=int(input())
while(n):
    if prime(n):
        print(n)
        break;
    else:
        n=n+1
        prime(n)]]]
method 2:
n=int(input())
while(1):
    c=0
    for i in range(2,(n//2)+1):
        if(n%i==0):
            c=c+1
    if c==0:
        print(n)
        break;
    else:
        n=n+1
    print(i)


###for i in range(1,n+1):
for i in range(2,n)
for i in range(2,(n//2)+1)###

n=int(input())
while(1):
    c=0
    for i in range(2,(n//2)+1):
        if(n%i==0):
            c=c+1
            break
    if(c==0):
        print(n)
        break  
    else:
        n=n+1'''


ii)ip:7854
op:2

n=int(input())
c=0
while(n):
    if(n%10 in [2,3,5,7]):
        c=c+1
    n=n//10
print(c)



    
    
