'''ip:
    "abfgresagtyuiofde"
longest substring:
    resagtyuiofd'''

str=input()
d={}
s=""
m=0
i=0
while(i<len(str)):#if i goes outside it will break loop
    while(i<len(str)):
        if (str[i] not in s):
            s=s+str[i]
            d[s[i]]=i#index of first occurence
        else:
            if(len(str)>m):
                m=len(s)
            s=""
            break
        i=i+1
    i=d[str[i]]+1 #from where it should run again
print(m)    

