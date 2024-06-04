'''PASSWORD
1 upper
1 lower
length 8
digit 1
special character 1
op:
valid or not

ip:
asd123!@#
op:
1

ip:
123456789
op:
3

ip:
ab
op:
6

ip:
A1234B
op:
2

'''


n=input()
u,l,s,d=0,0,0,0
for i in n:
    if(i.isdigit()):
        d=1
    elif(i.islower()):
        l=1
    elif(i.isupper()):
        u=1
    else:
        s=1
m=4-(u+l+d+s)
if(len(n)+m)<=8:
    print(8-len(n))
else:
    print(m)

### Examples:
1. **Input: asd123!@#**
   - u = 0, l = 1, s = 1, d = 1
   - m = 4 - (0 + 1 + 1 + 1) = 1
   - len(n) + m = 9 + 1 = 10
   - Output: 1

2. **Input: 123456789**
   - u = 0, l = 0, s = 0, d = 1
   - m = 4 - (0 + 0 + 0 + 1) = 3
   - len(n) + m = 9 + 3 = 12
   - Output: 3

3. **Input: ab**
   - u = 0, l = 1, s = 0, d = 0
   - m = 4 - (0 + 1 + 0 + 0) = 3
   - len(n) + m = 2 + 3 = 5
   - 8 - len(n) = 8 - 2 = 6
   - Output: 6

4. **Input: A1234B**
   - u = 1, l = 0, s = 0, d = 1
   - m = 4 - (1 + 0 + 0 + 1) = 2
   - len(n) + m = 6 + 2 = 8
   - Output: 2

    
