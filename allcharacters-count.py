'''a=input()
u,l,d,s=0,0,0,0
for i in a:
    if(i.isupper()):
        u=u+1
    elif(i.islower()):
        l=l+1
    elif(i.isdigit()):
        d=d+1
    else:
        s=s+1
 to count special character directly 
not i.isalnum()
 alphabets and numbers
i.isalnum()'''


a=input()
uv,uc,lv,lc,d,s=0,0,0,0,0,0
for i in a:
    if(i.isupper()):
        if(i in 'AEIOU'):
            uv=uv+1
        else:
            uc=uc+1
    elif(i.islower()):
        if(i in 'aeiou'):
            lv=lv+1
        else:
            lc=lc+1
    elif(i.isdigit()):
        d=d+1
    else:
        s=s+1
print("uv-",uv)
print("uc-",uc)
print("lv-",lv)
print("lc-",lc)
print("d-",d)
print("s-",s)


str1=input()
uc,uvc,lc,lvc,dc,sc=0,0,0,0,0,0
for i in str1:
    if(i.isupper()):
        if(i in 'AEIOU'):
            uvc=uvc+1
        else:
            uc=uc+1
    elif(i.islower()):
        if(i in 'aeiou'):
            lvc=lvc+1
        else:
            lc=lc+1
    elif(not i.isalnum()):
        sc=sc+1
    else:
        dc=dc+1
print("uc-",uc,"uvc-",uvc,"lc-",lc,"lvc-",lvc,"dc-",dc,"sc-",sc)



