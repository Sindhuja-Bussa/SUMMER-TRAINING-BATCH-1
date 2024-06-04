'''ip:
    5
op:
    *****
    *123*
    *456*
    *789*
    *****'''
'''n=int(input())
k=1
for i in range(n):          
    for j in range(n):
        if(i==0 or i==n-1 or j==0 or j==n-1):
            print("*",end=" ")
        else:
            print(k,end=" ")
            k=k+1
            
    
    print()'''


ip:
    4
op:
    _ _ _ _ a _ _ _ _
    _ _ _ a b a _ _ _
    _ _ a b c b a _ _
    _ a b c d c b a _

n=int(input())
for i in range(n):
    for j in range(n-i):
        print("_",end=" ")
    for i in range(n):
        s=chr(ord('a'))+i
        
    for i in range(n-i):
        print("_",end=" ")
    print()

ip:
    4
op:
    _ _ _ _ a _ _ _ _
    _ _ _ a b a _ _ _
    _ _ a b c b a _ _
    _ a b c d c b a _
n=int(input())
s=''
r=''
f=''
k=1
for i in range(n):
    print('-'*(n-i),end="")
    s=f+chr(ord('a')+i)+r
    r=f[::-1]
    f=f+chr(ord('a')+i)
    print(s,end="")
    print('-'*(n-i),end="")
    print()


    
      

        



      
      
      

      
      
      

     
        
        
