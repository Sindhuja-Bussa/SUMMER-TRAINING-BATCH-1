'''a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=a+b
c.sort()
print(c)'''


a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=[]
i,j=0,0
while(i<len(a) and j<len(b)):
    if(a[i]<b[j]):
        c.append(a[i])
        i=i+1
    else:
        c.append(b[j])
        j=j+1
'''
 for remaining elements in j 10,13
while(j<len(b)):
    c.append(b[j])
    j=j+1
while(i<len(a)):
    c.append(a[i])
    i=i+1
print(c)

it mixes two lists together '''
if(j<len(b)):
    c.extend(b[j:])
if(i<len(a)):
    c.extend(a[i:])
print(c)


    
    
