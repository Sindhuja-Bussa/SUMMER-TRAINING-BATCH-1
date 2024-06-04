'''print sum of even numbers in two lists
ip:
    a=[3,8,5,4,3] add all even no
    b=[5,0,9,3,2] add all odd no
op:
    (12,17)'''
def fun1(x,s):
    if(x==len(a)):
        return s
    if(a[x]%2==0):
        s=s+a[x]
    t=fun1(x+1,s)
    return t
    


def fun2(z,su):
    if(z==len(b)):
        return su
    if(b[z]%2!=0):
        su=su+b[z]
    s=fun2(z+1,su)
    return s

a=list(map(int,input().split()))
b=list(map(int,input().split()))
x=fun1(0,0))
y=fun2(0,0))
print(x,y)

def fun(i,s1,s2):
    if(i==len(a)):
        return s1,s2
    if(a[i]==0):
        s1=s1+a[x]
    if(b[i]!=0):
        s2=s2+b[x]
    return fun(i+1,s1,s2)    
a=list(map(int,input().split()))
b=list(map(int,input().split()))
x,y=fun(i+1,s1,s2)
print(f(0,0,0))
    
