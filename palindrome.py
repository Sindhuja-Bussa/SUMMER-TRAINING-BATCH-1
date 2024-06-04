
def pal(n,rev):
    if(n==0):
        return rev
    x=n%10
    rev=(rev*10)+x
    return pal(n//10,rev)
n=int(input())
r=pal(n,0)
if(n==r):
    print("palindrome")
else:
    print("no")
    




    
