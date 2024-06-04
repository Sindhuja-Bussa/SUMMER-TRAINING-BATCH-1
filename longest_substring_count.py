'''ip:
    "xyzabcdefklmnopqefgh"
op:
    print the longest sequence substring
    abcdef
    length=7(output)'''
'''coz j i+1 will be index out of range'''
str=input()
count=1
m=0
for i in range(len(str)-1):
    if ord(str[i])==ord(str[i+1])-1:
        count=count+1
        if(count>m):
            m=count
    else:
        count=1
'''if(count>m):
    m=count '''
print(m)

''' xyabcde the ans at last is 2
abcde is 0 for that we need to keep if condition'''
        



