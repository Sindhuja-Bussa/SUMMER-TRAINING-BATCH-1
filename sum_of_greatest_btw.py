'''
ip:
[4,8,14,22,37,68]
op:
sum of primes between them'''
def lprime(m,n):
    for i in range(n-1,m,-1):
        if(isPrime(i)):
            return i
    return 0
def isPrime(i):
    for k in range(2,(i//2)+1):
        if i%k==0:
            return 0
    return 1
l=[4,8,14,22,37,68]
s=0
for i in range(len(l)-1):
    s= s + lprime(l[i],l[i+1])
print(s)

