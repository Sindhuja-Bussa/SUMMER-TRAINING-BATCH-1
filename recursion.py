def fun(x):
    if(x==6):
        return
    print(x)
    fun(x+1)
fun(1)
print("hi")

op: 1 2 3 4 5 hi

'''def fun():
    print("hi")
    fun()
fun()'''

def fun(x):
    print(x)
    fun(x+1)
fun(1)





def fun(x):
    if(x==6):
        return //this return will go to last line(1,1+1,2+1,3+1,4+1,5+1)
    print(x)
    fun(x+1)
    print(x)
fun(1)
print("hi")
op:1 2 3 4 5 5 4 3 2 1 hi
    
def fun(x):
    if(x==3):
        return 500
    print(x)
    t=fun(x+1)
    print(x)
    return t
    //return 100

print(fun(1))
op: 1 2 2 1 500

//print
def fun(x):
    if(x==len(a)):
        return
    print(a[x])
    fun(x+1)
a=[6,7,2,4]
fun(0)

//sum
def fun(x):
    s=0
    if(x==len(a)):
        print(s)
        return
    s=s+a[x]
    fun(x+1)
a=[6,7,2,4]
fun(0)
op:0

//sum
def fun(x,s):
    if(x==len(a)):
        print(s)
        return
    s=s+a[x]
    fun(x+1,s)
a=[6,7,2,4]
fun(0,0)
op:20

//sum
def fun(x,s):
    if(x==len(a)):
        return s // go to fun(x+1,s)
    s=s+a[x]
    fun(x+1,s)
a=[6,7,2,4]
fun(0,0)

//sum
def fun(x,s):
    if(x==len(a)):
        return s // go to fun(x+1,s)
    s=s+a[x]
    t=fun(x+1,s) or return fun(x+1,s)
    return t
a=[6,7,2,4]
print(fun(0,0))//receive 20
