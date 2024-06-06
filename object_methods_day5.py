class Node:
    a=5
    def __init__(self):
        self.b=60
x.node()
print(a)
#error->a is not defined, outside the class that's y python is object oriented

class Node:
    a=5
    def __init__(self):
        self.b=60
x.node()
print(x.a)#5
print(x.b)#60
#object.variable

class Node:
    a=5
    def __init__(self):
        self.b=60
x.node()
print(node.a) #5
print(node.b) #error(coz b is more secured than a(x.b object only 
#object.variable

class Node:
    a=5
    def asd():
        print("hi")
    def __init__(self):
        self.b=60
x=node()
asd()#error
x.asd()#it takes 0 arguments->error

class Node:
    a=5
    def asd(self):
        print("hi")
    def __init__(self):
        self.b=60
x=node()
asd()#error
x.asd()#it takes 0 arguments->error
node.asd()#hi

class Node:
    a=5
    def asd():
        print("hi")
    def __init__(self):
        self.b=60
    def qwer(self):
        print("hello")
x=node()
node.qwer(10) #hello

class Node:
    a=5
    def asd():
        print("hi")
    def __init__(self):
        self.b=60
    def qwer(self):
        print("hello",self.x)
x=node()
node.qwer(10,20) #hello 10 20

class Node:
    a=5
    def asd():#static method can be access with object only
        print("hi")
    def __init__(self):
        self.b=60
    def qwer(cse,x):#non static method (can be access with class name)
        print("hello",cse.b,x)
x=node()
node.qwer(x,20) #hello 60 20
