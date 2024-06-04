def num(x):
    if x==0:
        return 0
    return x+num(x-2)
'''10+8
18+6
24+4
odd:
13
13+11(odd number is adding
so do n-1
12+10
12+8
'''
n=int(input())
if(n%2==0):
    print(num(n)
else:
    print(num(n-1))

