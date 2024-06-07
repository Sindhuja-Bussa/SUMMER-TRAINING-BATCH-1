n=int(input())
list1=[]
for i in range(n):
    list1.append(int(input()))
s=0
sum1=(n*(n+1))//2
for i in list1:
    s=s+i
s1=sum1-s
print(s1)
    

