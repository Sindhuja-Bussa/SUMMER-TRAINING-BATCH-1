n=input()
count1=0
count2=0
for i in n:
    if(i=='M'):
        count1=count1+1
    elif(i=='F'):
        count2=count2+1
if(count1==count2):
   print("0")
elif(count1>count2):
    print("M")
else:
    print("F")

c=0
for i in a:
    if(i=='M'):
        c=c+1
    else:
        c=c-1

