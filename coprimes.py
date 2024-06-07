'''n=int(input())
m=int(input())
def gcd(x,y):
    if(y==0):
        return x
    else:
        gcd(y,x%y)

x=int(input())
y=int(input())
z=gcd(x,y)
if(z==1):
    print("co-primes")
else:
    print("not co-primes")'''



'''import math
a=2
b=3
x=math.gcd(a,b)
if(x==1):
    print("co-primes")
else:
    print("not co-primes")
'''
#coprimes
a=int(input())
b=int(input())
for i in range(2,(min(a,b)//2+1)):
    if a%i==0 and b%i==0:
        print('ncp')
        break
    else:
        print('cp')



'''#coprimes
a=int(input())
b=int(input())
for i in range(2,(min(a,b)//2+1)):
    if a%i==0 and b%i==0:
        print('ncp')
        break
    else:
        print('cp')'''

