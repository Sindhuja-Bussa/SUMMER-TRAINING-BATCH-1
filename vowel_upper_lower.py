'''ip:
    placements
op:
    plAcEmEnts'''
str1=input()
v=['a','e','i','o','u','A','E','I','O','U']
b=''
for i in str1:
    if i in v:
        i=i.upper()
        b=b+i
    else:
        b=b+i
print(b)
        

