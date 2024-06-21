#Sort Respect to length

#Method 1
'''a=["school","car","apple","hi",'hat']#if extra 3 len word it will print car only
b=[]
for i in a:
    b.append(len(i))
print(b)#[6, 3, 5, 2]
c=b.copy()
c.sort()
print(c)#[2, 3, 5, 6]
for i in c:
    print(a[b.index(i)])
op:
    hi
    car
    apple
    school

#Method 2
a=["school","car","apple","hi"]
b=[]
for i in a:
    b.append(len(i))
c=list(zip(b,a))#it will merge b and a elements
c.sort()
for i,j in c:
    print(j)
    
#method 3
a=["school","car","apple","hi","hat"]
a.sort(key=len)
print(a)'''


#Sort Respect to 2nd element
'''def fun(x):
    return x[1]
a=["school","car","apple","hi","hat"]
a.sort(key=fun)
print(a)'''


#Sort Respect to sum
'''def fun(x):
    return sum(x)
a=[[3,15],[7,3],[12,8],[9,3],[5,6]]
a.sort(key=fun)
print(a)'''


'''a=[[3,15],[7,3],[12,8],[9,3],[5,6]]
a.sort(key=sum)
print(a)'''

#Sort Respect to max
'''a=[[3,15],[7,3],[12,8],[9,3],[5,6]]#max of each one->15,7,12,9,6
a.sort(key=max)
print(a)#[[5, 6], [7, 3], [9, 3], [12, 8], [3, 15]]'''

#Sort Respect to min
a=[[3,15],[7,3],[12,8],[9,3],[5,6]]
a.sort(key=min)
print(a)#[[3, 15], [7, 3], [9, 3], [5, 6], [12, 8]]


