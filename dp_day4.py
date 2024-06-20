'''ip:
    no.of queries 7
    1 school
    1 world
    1 word
    1 scholar
    2 word
    2 wood
    3 sch
op:
True(word)
False(wood)
True(sch)'''
'''7
1
school
1
world
1
word
1
scholar
2
word
true
2
wood
false
3
sch
true'''
'''n=int(input())
l=[]
for i in range(1,n+1):
    a=int(input())
    b=input()
    if(a==1):
        l.append(b)
    elif(a==2):
        if b in l:
            print("true")
        else:
            print("false")
    elif(a==3):
        for i in range(len(l)):
            if b in l[i]:
                print("true")
                break
        else:
            print("false")
    elif(a==4):
        if b in l:
            l.remove(b)
print(l)'''
'''7
1
school
1
world
1
word
1
scholar
2
word
true
3
sch
2
4
word
['school', 'world', 'scholar']   '''
            
                      
            
'''n=int(input())
l=[]
for i in range(1,n+1):
    a=int(input())
    b=input()
    if(a==1):
        l.append(b)
    elif(a==2):
        if b in l:
            print("true")
        else:
            print("false")
    elif(a==3):
        c=0
        for i in range(len(l)):
            if b in l[i]:
                c=c+1
        print(c)
    elif(a==4):
        if b in l:
          l.remove(b)
        print(l)'''
    
'''5
1
word
1
word
3
wo
1
4
word
[]
2
word
false   '''

n=int(input())
l=[]
for i in range(1,n+1):
    a=int(input())
    b=input()
    if(a==1):
        if b not in l:
            l.append(b)
    elif(a==2):
        if b in l:
            print("true")
        else:
            print("false")
    elif(a==3):
        c=0
        for i in range(len(l)):#for i in l:
            #if i.startswith(b)
            if b in l[i]:
                c=c+1
        print(c)
    elif(a==4):
        if b in l:
          l.remove(b)
        print(l)
        

    
            
            
            
            
            
        
    
        

    



    
