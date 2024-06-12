'''ip:
    "hello:5438,car:214,book:8799,apple:2187"

op:
    oaxp'''
l=input().split(',')
print(l)
a=''
for i in l:
    b=i.split(':')
    print(b)
    c=len(b[0])
    print(b[0],b[1])
    if (str(c) in b[1]):
        a=a+b[0][-1]
    else:
        for i in range(c-1,0,-1):
            if(str(i) in b[1]):
                a=a+b[0][i-1]
                break
        else:
            a=a+'x'
print(a)
