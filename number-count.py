a=list(map(int,input().split()))
b=[]
''' for unique elements in a'''
for i in a:
    if(i not in b):
        b.append(i)

for i in b:
    print(i,"-",a.count(i))
        
