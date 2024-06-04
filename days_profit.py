'''list1=list(map(int,input().split()))
m=0
for i in range(len(list1)-1):
    for j in range(i+1,len(list1)):
        n=list1[i]-list1[j]
        if(m>n):
            m=n
print(abs(m))'''


'''a=list(map(int,input().split()))
m=0
for i in range(len(a)-1):
    for j in range(i+1,len(a)):
        if(a[i]<a[j] and a[j]-a[i]>m):
            m=a[j]-a[i]
print(m)'''
            
        
a=list(map(int,input().split()))
m=[]
for i in range(len(a)-1):
    for j in range(i+1,len(a)):
        if(a[i]<a[j] and a[j]-a[i]>m):
            m.append(a[j]-a[i])
print(max(m))

'''o(n)'''
a=list(map(int,input().split()))
b=0'''(updating bying price)'''
for i in range(len(a)):
    
    
