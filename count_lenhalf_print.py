'''i)ip:
    [4,8,2,4,4,4,8]
op:
    len=7,7/2=3.5
    4=4 times(more than 3.5)
    print(i)'''


'''list1=list(map(int,input().split()))
h=(len(list1)//2)
for i in list1:
    c=list1.count(i)
    if(c>h):
        f=i
    else:
        f="invalid input"
print(f)'''

'''list1=list(map(int,input().split()))
b=[]
h=(len(list1)//2)
for i in list1:
    if(i not in b):
        b.append(i)
for i in b:
    c=list1.count(i)
    if(c>h):
        f=i
        break
    else:
        f="invalid input"
print(f)'''


'''2)[122221]
winner=1,curr=1
1->+
2->-(change 1 to 2)if zero'''

list1=list(map(int,input().split()))
c=1
w=list1[0]
for i in range(1,len(list1)):
    if(list[i]==w):
        c=c+1
    else:
        c=c-1
        #c=c-1(if diff elements going to negative values)
        if(c==0):
            c=1
            w=list1[i]
print(w)

'''list1=list(map(int,input().split()))
c=1
w=0
for i in range(len(list1)):
    if(list[i]==list[i-1]):
        c=c+1
    else:
        c=c-1
        #c=c-1(if diff elements going to negative values)
        if(c==0):
            c=1
            w=list1[i]
print(w)'''
    

    
    


        
    
        
    
    
