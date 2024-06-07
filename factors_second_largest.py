'''n=int(input())
k=int(input())
l=[]
for i in range(1,n+1):
    if(n%i==0):
        l.append(i)
print(l[-k])'''

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
    print("not co-primes")






    

    

        
    
