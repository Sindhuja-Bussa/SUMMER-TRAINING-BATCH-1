'''ip:
    [4,9,8,2,14,3,5,6]
    (4,8,9) (9,8,2)(2,14,3) (3,5,36)
    sort 3 numbers combinations'''
#sort using min
a=[4,9,8,2,14,3,5,6]
#print(a)
for i in range(len(a)):
    j=i+2
    m=a[i:j+1]
    #print(m)
    m1=a.index(min(m))
    a[i],a[m1]=a[m1],a[i]
    j=j+1
print(a)
