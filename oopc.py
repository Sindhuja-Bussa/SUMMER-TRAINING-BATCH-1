class qwer:
    def __int__(self,v,u):
        self.a=u
        self.b=v
    def asd(self,x):
        print("hello",self.a)
        x.zxc()
    def zxc(self):
        print("hi",self.b)
x=qwer(20,40)
y=qwer(50,10)
y.asd()

'''hello 10
hi 20

qwer.asd(x)=y.asd(x)'''

class qwer:
    def __int__(self,v,u):
        self.a=u
        self.b=v
    def asd(self,x):
        print("hello",self.a)
        x.zxc()
    def zxc(self):
        print("hi",self.b)
x=qwer(20,40)
y=qwer(50,10)
y.asd(x)
'''hello 40
hi 20'''

class qwer:
    def __int__(self,v,u):
        self.a=u
        self.b=v
    def asd(self,x):
        print("hello",self.a)
        x.zxc()
    def zxc(self):
        print("hi",self.b)
x=qwer(20,40)
y=qwer(50,10)
y.asd(x)

'''hello 40
hi 50'''

class qwer:
    def __int__(self,u,v):
        self.a=u
        self.b=v
    def asd(self,x):
        print("hello",self.a+x,self.b)
        y.zxc(x+10)
    def zxc(self,y):
        print("hi",self.b+y,self.a)
x=qwer(40,10)
y=qwer(50,10)
x.asd(60)

'''hello 100 10
hi 80 50'''

class qwer:
    def __int__(self,u,v):
        self.a=u
        self.b=v
    def fun(self,x):
        print("hello")

class asd:
    def fun1(self):
        print("hi")

x=qwer(40,10)
y.asd()
'''hi
y.fun->error'''

class qwer:
    def __int__(self,u,v):
        self.a=u
        self.b=v
    def fun(self,x):
        print("hello")

class asd(qwer):
    def fun(self):
        print("hi")
y=asd(40,10)
y.fun(20)

'''error'''
class qwer:
    def __int__(self,u,v):
        self.a=u
        self.b=v
    def fun(self,x):
        print("hello")

class asd(qwer):
    def fun(self):
        print("hi",self.a)
x=qwer(40,10)
y=asd(80,10)
y.fun()
''' hi 80'''

class A:
    pass
class B(A):
    pass
class C(A):
    pass
'''hierarchical inheritance'''

class A:
    pass
class B:
    pass
class C(A,B):
    pass
'''multiple inheritance'''

class A:
    pass
class B(A):
    pass
class C(B):
    pass
'''multilevel inheritance'''


class A:
    def fun(self):
        print("hi")
class B:
    def fun(self):
        print("hey")
class C(A,B):
     def fun(self):
        print("hello")
x=c()
x.fun()
'''hello'''

class A:
    def fun(self):
        print("hi")
class B:
    def fun(self):
        print("hey")
class C(A,B):
     def fun1(self):
        print("hello")
x=c()
x.fun()
'''hi'''


class A:
    def fun(self):
        print("hi")
class B:
    def fun(self):
        print("hey")
class C(B,A):
     def fun1(self):
        print("hello")
x=c()
x.fun()
'''hey'''
