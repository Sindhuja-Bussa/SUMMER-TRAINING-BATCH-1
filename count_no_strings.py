a=input()
count=1
b=''
for i in range(len(a)-1):
    if(a[i]==a[i+1]):
        count=count+1
    else:
        b=b+a[i]+str(count)
        count=1
''' for d statement '''
b=b+a[i]+str(count)
print(b)

    
    
