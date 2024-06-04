'''nums=list(map(int,input().split()))
rsum=0
j=nums[-1]=0
n=len(nums)
i=nums[0]=0
for i in range(n):
    rsum=rsum+i
    print(rsum)
b=[]
for i in range(len(a)):
    
b.append(abs(sum(a[:i]))-(sum(a[i+1:]))

a=input().split()
r=[0]*len(a)
for i in a:
    r[int(i[-1])-1]=i[:-1]
return ''.join(r)
ip:
khoor
3
op:
hello'''

'''s=input()
n=int(input())
c=n%26
a=""
for i in s:
    b=ord(i)-c
    if(b>=97):
        a=a+chr(b)
    else:
        a=a+chr(b+26)
print(a)'''


'''n=int(input())
m=[]
flag=1
for i in range(n):
    for j in range(n):
        m.append(input())
str=input()
for i in range(len(str)):
    if(str[i] in m[i%n]):
        continue
    else:
        flag=0
        break
if(flag==0):
    print("no")
else:
    print("yes")'''

'''n=int(input())
m=[]
flag=1
for i in range(n):
    for j in range(n):
        m.append(list(input()))
str=input()
for i in range(len(str)):
    if(str[i] not in m[i%n]):
        flag=0
        break
    else:
        m[i].remove(str[i])   
if(flag==1):
    print("yes")
else:
    print("no")'''

    
input:
    a
output: 
    ----a----
    ---aba---
    --abcba--
    -abcdcba-'''

n = int(input())
for i in range(n):
  for j in range(n-i):
    print("_", end=" ")
  for i in range(n):
    s = chr(ord('a') + i)
    print(s, end=" ")
  for i in range(n-i-1):
    s = chr(ord('a') + n - i - 1)
    print(s, end=" ")
  for i in range(n-i):
      print("_", end=" ")

  print()

    



