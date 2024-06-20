#Sun falling
'''
l=1 3 9 8 6 10
left=1 3 9 9 9 10
right=10 10 10 10 10'''
'''l=list(map(int,input().split()))
left=l.copy()
right=l.copy()
for i in range(len(left)-1):
    if(left[i]>left[i+1]):
        left[i+1]=left[i]
for i in range(len(right)-1,-1,-1):
    if(right[i]>right[i-1]):
        right[i-1]=right[i]           
print(list(set(left)))
print(list(set(right)))'''
    

#coins
#l=[2,3,5,6]
#output:if we add any numbers it should print x
l=list(map(int,input().split()))
x=int(input())#11
flag=0
for i in range(len(l)-1):
    s=0
    for j in range(1,len(l)):
        s=sum(l[i:j+1])
        if(s==x):
            flag=1
        else:
            flag=0
if(flag==1):
    print("yes")
else:
    print("no")

#coins_dp
l=list(map(int,input().split()))
x=int(input())
m=[]
for i in range(len(l)+1):
    m.append([0]*m+1)
for i in range(1,len(matrix)+1):
    for j in range(1,x+1):
        if(m[i]==0):
            m[i][j]=1
        elif(m[i]==i):
            m
        
        
        

m=[2,3,5,6]
n=11 
fun()

