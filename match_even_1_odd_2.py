'''l1=[6,3,2,9,4,7]
l2=[8,7,5,3,6,9]
res=[13,11,9,15,9,7,5,11,11,9,7,13]'''

def match(l1,l2,l3,i,j):
    if i==len(l1):
        return l3
    def match1(l1,l2,l3,i,j):
        if(j=len(l2)):
            if l1[i]%2==0:
                if l2[j]%2!=0:
                    s=s+l1[i]+l2[j]
                    l3.append(s)
                    s=0
                else:
                    j+=1
        return match1(l1,l2,l3,i+1,j)
    return match(l1,l2,l3,i+1,j)
l1=[6,3,2,9,4,7]
l2=[8,7,5,3,6,9]
print(match(l1,l2,[],0,0))


'''l1=[6,3,2,9,4,7]
l2=[8,7,5,3,6,9]
l3=[]
l4=[]
i=0
j=0
while(i==len(l1)):
    if(l1[i]%2==0):
        l3.append(l1[j])
    else:
        l1[i]=l1[i]+1
print(l3)
while(j==len(l2)):
    if(l2[j]%2!=0):
        l4.append(l2[j])
    else:
        l2[i]=l2[i]+1
print(l4)
'''s=0
while(l3):
    while(l4):
        s=s+l3[i]+l4[j]
        print(s)
        i=i+1
        j=j+1'''
        
        

