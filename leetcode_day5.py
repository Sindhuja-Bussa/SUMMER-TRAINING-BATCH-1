'''1221
3120
520
3121''''


class Solution:
    def balancedStringSplit(self, s: str) -> int:
        c=0
        max=0
        for i in s:
                if(i=='R'):
                    c=c+1
                if(i=='L'):
                    c=c-1
                if(c==0):
                    max=max+1
                    c=0
        return max

class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        b=""
        c=0
        for i in word:
            if(i not in b):
                b=b+i
        for i in b:
            if(i==i.lower()):
                j=i.upper()
                if j in b:
                    c=c+1
            elif(i==i.upper()):
                j=i.lower()
                if j in b:
                    c=c+1
        return c//2

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        '''a="USA"
        pf(a.isupper())
        return True'''

        '''a="usa"
           pf(a.islower())
           return False'''

        '''a=USA
           a=Usa
           print(a.istitle())'''
        for i in word:
            if(word.isupper() or word.islower() or word.istitle()):
                return True
            return False


class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        '''a=aaAaA
        print(a.index("A"),a.rindex('a))
        index->fist index occurence
        rindex->last index occurence'''
        a=""
        c=0
        for i in word:
            if(i.islower() and i not in a and i.upper() in word):
                a=a+i
                if(word.rindex(i) < word.index(i.upper())):
                    c=c+1
        return c
