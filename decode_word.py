'''ip:
    khoor
    3
op:
    hello'''
str=input()
n=int(input())
c=n%26
d=""
for i in str:
    b=ord(i)-c
    if(b>=97):
        d=d+chr(b)
    else:
        d=d+chr(b+26)
print(d)



