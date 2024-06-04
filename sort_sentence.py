a=input().split()
r=[0]*len(a)
for i in a:
    r[int(i[-1])-1]=i[:-1]
return ''.join(r)
