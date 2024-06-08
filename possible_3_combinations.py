'''#to print all 3 combinations in the list
[3,2,5,4,1,6,8]
3 2 5
3 2 4
3 2 1
3 2 6
3 2 8.....'''

'''l=list(map(int,input().split()))
i,j,k=0,0,0
for i in range(len(l)):
    for j in range(i+1,len(l)):
        for k in range(i+2,len(l)):
            print(l[i],l[j],l[k],end=" ")
            print()'''
            
                
'''#recursion

def three_comb(l,i,j,k):
    if k==len(l):
        return 
    if(i!=len(l)-2 and j!=len(l)-1 and k!=len(l)):
       print(l[i],l[j],l[k],end=" ")
       print()
    return three_comb(l,i+1,j+1,k+1)
l=list(map(int,input().split()))
print(three_comb(l,0,1,2))'''


def combination(l,k):
    def fun(curr,start):
        if(len(curr)==k):
            print(curr)
            return
        for i in range(start,len(l)):
            fun(curr+[l[i]],i+1)
        return
    fun([],0)
a=[3,5,1,6]
k=3
combination(a,k)


