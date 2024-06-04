
def sum(n):
    sum1=0
    while(n):
        x=n%10
        sum1=sum1+x
        n=n//10
    return sum1
def pnp(p):
    if(n in [2,3,5,7]):
        return m
    else:
        return m+1
n=int(input())
m=n
if(n<10):
    print(pnp(n))
else:
        while(1):
            n=sum(n)
            if(n<10):
                break
        print(pnp(n))
    
'''while():
    if(n<10):
        print(pnp(n))
    else:
        while(1):
            n=sum(n)
            if(n<10):
                break
        print(pnp(n))
n=input()
m=sum(list(ma(int,n)))
print(m)'''

