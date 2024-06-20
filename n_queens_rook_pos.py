#N-QUEENS
def queen(r):
    if r==n:
        return
    if(r!=a):
        for c in range(n):
            if check(r,c):
                m[r][c]='q'
                break
            m[r][c]=0
        return queen(r+1)
    else:
        queen(r+1)
def check(i,j):
    if j==b:
        return 0
    r=i
    c=j
    for i in range(j+1):
        if m[i][j]=='q':
            return 0
    i=r
    while(i>=0 and j>=0):#up right diagonal
        if m[i][j]=='q':
            return 0
        i=i-1
        j=j-1
    while(r>=0 and c<n):#up left diagonal
        if m[i][j]=='q':
            return 0
        r=r-1
        c=c+1
    return 1
n=int(input())
#rook position
a=int(input())
b=int(input())
m=[]
for i in range(n):
    m.append([0]*n)
queen(0)
print(m)
c=0
for i in m:
    if(i=='q'):
        c=c+1
print(c)





'''def Nqueen(board,r,r1,c1):
    if r==len(board):
        return 
    if r!=r1:
        for c in range(len(board)):
            if issafe(board,r,c,c1):
                board[r][c]="1"
                break
        
            board[r][c]='0'
        return Nqueen(board,r+1,r1,c1)

    else:
        Nqueen(board,r+1,r1,c1)
def issafe(board,r,c,c1):
    for i in range(r):
        if c==c1:
            return False
        if board[i][c]=="1":
            return False
        
    i,j=r,c
    while i>=0 and j<len(board):
        if board[i][j]=="1":
            return False
        i=i-1
        j=j+1
    i,j=r,c
    while i>=0 and j>=0:
        if board[i][j]=="1":
            return False
        i=i-1
        j=j-1
    return True
n=int(input("enter number of queens:"))
r1=int(input())
c1=int(input())
board=[["0" for i in range(n)] for j in range(n)]
Nqueen(board,0,r1,c1)
for i in board:
        print("".join(i))
