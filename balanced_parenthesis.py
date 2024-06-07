def balanced(s):
    st=[]
    for i in s:
        if i=='(' or i=='{' or i=='[':
            st.append(i)
        else:
            if not st:
                return False
            elif i==']' and st[-1]=='[':
                st.pop()
            elif i==')' and st[-1]=='(':
                st.pop()
            elif i=='}' and st[-1]=='{':
                st.pop()
            else:
                return False
    if not st:
        return True
    return False
s=input()
z=balanced(s)
print(z)


