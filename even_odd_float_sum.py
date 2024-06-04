list1=[5,3.8,7,5.6,4,2,3]
e,o,f=0,0,0.0
for i in list1:
    if isinstance(i,int):
        if(i%2==0):
            e=e+i
        else:
            o=o+i
    elif isinstance(i,float):
             f=f+i     
print("even sum-",e)
print("odd sum-",o)
print("float sum-",f)

ip:
    5,3.8,7,5.6,4,2,3
op:
    sum of odd = 15
    sum of even = 6
    sum of float = 9.4


'''if('.' in a)
for int=5
print(a%1)=0
for float=7.4
b%1= 0.40000000036'''
    
